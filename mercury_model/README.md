# MERCURY chatbot inference bundle

This folder contains everything needed to load the selected MERCURY checkpoint
and make predictions without the original `E:\Uni\RAMHA` project.

## Contents

- `best.pt`: complete trained model state
- `tokenizer/`: exact RoBERTa tokenizer files
- `encoder_config/`: offline RoBERTa-Large architecture configuration
- `mercury/model.py`: exact PyTorch inference architecture
- `mercury/inference.py`: checkpoint loading, preprocessing, and predictions
- `predict.py`: command-line example
- `api.py`: optional FastAPI endpoint
- `example_chatbot.py`: minimal conversational integration example
- `smoke_test.py`: end-to-end verification
- `config.json` and `labels.json`: architecture and class order
- `MODEL_CARD.md`: scope, results, and limitations
- `CHATBOT_INTEGRATION.md`: safe chatbot integration guidance
- `CHECKSUMS.sha256`: integrity hashes

## Setup

Use 64-bit Python. A CUDA-enabled PyTorch installation is recommended for
interactive latency; CPU inference works but is slow and uses substantial RAM.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If the exact CUDA build is unavailable from the default package index, install
the PyTorch build appropriate for the partner computer first, then install
`transformers==4.57.6 adapters==1.3.0 numpy==2.5.2`.

## One prediction

```powershell
python predict.py "I feel overwhelmed and tense because of work deadlines"
```

Exact Python usage:

```python
from mercury import MercuryPredictor

predictor = MercuryPredictor(device="auto")
result = predictor.predict("I cannot stop worrying about tomorrow.")
print(result["label"])
print(result["confidence"])
print(result["probabilities"])
```

## Verify the handoff

```powershell
python smoke_test.py
```

The first load can take time because the checkpoint is approximately 1.35 GB.
Keep one predictor instance alive for the lifetime of the chatbot process.
The harmless adapter-status warning sometimes printed during construction is
explained in `TROUBLESHOOTING.md`; the bundle was verified against the original
research loader and returned identical probabilities.

## Output meaning

The model always returns one of three inherited dataset categories. A high score
does not prove that a person has depression, anxiety, or stress. The model is
not validated for crisis detection and must not be used as a medical device.
