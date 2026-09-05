from __future__ import annotations

import torch
from torch import nn
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
from transformers import AutoConfig


class TokenAttention(nn.Module):
    def __init__(self, feature_size: int, attention_size: int = 512):
        super().__init__()
        self.projection = nn.Linear(feature_size, attention_size)
        self.context = nn.Parameter(torch.empty(attention_size))
        nn.init.normal_(self.context, mean=0.0, std=0.02)

    def forward(self, hidden: torch.Tensor, attention_mask: torch.Tensor):
        projected = torch.tanh(self.projection(hidden))
        scores = torch.matmul(projected, self.context)
        scores = scores.masked_fill(attention_mask == 0, torch.finfo(scores.dtype).min)
        weights = torch.softmax(scores, dim=1)
        context = torch.sum(hidden * weights.unsqueeze(-1), dim=1)
        return context, weights


class MercuryModel(nn.Module):
    """The exact deployable MERCURY/RAMHA inference architecture."""

    def __init__(
        self,
        encoder_config_dir: str,
        adapter_config: str = "seq_bn",
        hidden_size: int = 256,
        lstm_layers: int = 1,
        dropout: float = 0.5,
        num_classes: int = 3,
        pack_sequences: bool = False,
        attention_size: int = 512,
    ):
        super().__init__()
        from adapters import AutoAdapterModel

        config = AutoConfig.from_pretrained(encoder_config_dir, local_files_only=True)
        # best.pt contains every encoder parameter. Constructing from config avoids
        # downloading roberta-large merely to overwrite it with the checkpoint.
        self.encoder = AutoAdapterModel.from_config(config)
        self.encoder.add_adapter("ramha", config=adapter_config)
        self.encoder.set_active_adapters("ramha")
        self.pack_sequences = pack_sequences
        encoder_size = self.encoder.config.hidden_size
        self.bilstm = nn.LSTM(
            encoder_size,
            hidden_size,
            num_layers=lstm_layers,
            batch_first=True,
            bidirectional=True,
            dropout=dropout if lstm_layers > 1 else 0.0,
        )
        self.attention = TokenAttention(hidden_size * 2, attention_size)
        self.dropout = nn.Dropout(dropout)
        self.classifier = nn.Linear(hidden_size * 2, num_classes)

    def forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor):
        encoded = self.encoder.roberta(input_ids=input_ids, attention_mask=attention_mask)
        if self.pack_sequences:
            lengths = attention_mask.sum(dim=1).to("cpu")
            packed = pack_padded_sequence(
                encoded.last_hidden_state, lengths, batch_first=True, enforce_sorted=False
            )
            packed_sequence, _ = self.bilstm(packed)
            sequence, _ = pad_packed_sequence(
                packed_sequence, batch_first=True, total_length=attention_mask.size(1)
            )
        else:
            sequence, _ = self.bilstm(encoded.last_hidden_state)
        context, weights = self.attention(sequence, attention_mask)
        logits = self.classifier(self.dropout(context))
        return {"logits": logits, "attention_weights": weights}
