from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable

import torch
from transformers import AutoTokenizer

from .model import MercuryModel


def clean_text(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", str(text))
    text = re.sub(r"[^\w\s']", " ", text)
    return re.sub(r"\s+", " ", text).strip()


class MercuryPredictor:
    """Load MERCURY once and reuse it for chatbot requests."""

    def __init__(self, bundle_dir: str | Path | None = None, device: str = "auto"):
        self.bundle_dir = Path(bundle_dir or Path(__file__).resolve().parents[1])
        self.config = json.loads((self.bundle_dir / "config.json").read_text(encoding="utf-8"))
        self.labels = json.loads((self.bundle_dir / "labels.json").read_text(encoding="utf-8"))["labels"]
        self.device = torch.device(
            ("cuda" if torch.cuda.is_available() else "cpu") if device == "auto" else device
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.bundle_dir / "tokenizer", local_files_only=True
        )
        m = self.config["model"]
        self.model = MercuryModel(
            str(self.bundle_dir / "encoder_config"),
            adapter_config=m["adapter_config"],
            hidden_size=m["lstm_hidden_size"],
            lstm_layers=m["lstm_layers"],
            dropout=m["dropout"],
            num_classes=m["num_classes"],
            pack_sequences=m["pack_sequences"],
            attention_size=m["attention_hidden_size"],
        )
        checkpoint = torch.load(
            self.bundle_dir / "best.pt", map_location="cpu", weights_only=True
        )
        # The training library attached an unused default language-model head.
        # MERCURY calls encoder.roberta directly, so those six tensors never
        # participate in inference and are intentionally excluded here.
        model_state = {
            key: value
            for key, value in checkpoint["model_state"].items()
            if not key.startswith("encoder.heads.default.")
        }
        missing, unexpected = self.model.load_state_dict(model_state, strict=True)
        if missing or unexpected:
            raise RuntimeError(f"Checkpoint mismatch: missing={missing}, unexpected={unexpected}")
        self.model.to(self.device).eval()

    @torch.inference_mode()
    def predict(self, text: str, clean: bool = True) -> dict:
        original = str(text)
        model_text = clean_text(original) if clean else original.strip()
        if not model_text:
            raise ValueError("Text is empty after preprocessing.")
        encoded = self.tokenizer(
            model_text,
            truncation=True,
            padding="max_length",
            max_length=self.config["model"]["max_length"],
            return_tensors="pt",
        )
        encoded = {k: v.to(self.device) for k, v in encoded.items() if k in {"input_ids", "attention_mask"}}
        output = self.model(**encoded)
        probabilities = torch.softmax(output["logits"], dim=-1)[0].cpu()
        predicted_id = int(probabilities.argmax())
        return {
            "label": self.labels[predicted_id],
            "label_id": predicted_id,
            "confidence": float(probabilities[predicted_id]),
            "probabilities": {
                label: float(probabilities[i]) for i, label in enumerate(self.labels)
            },
            "cleaned_text": model_text,
            "disclaimer": "Research classification only; not a diagnosis or clinical recommendation.",
        }

    def predict_batch(self, texts: Iterable[str], clean: bool = True) -> list[dict]:
        return [self.predict(text, clean=clean) for text in texts]
