# Chatbot integration

Load `MercuryPredictor` once when the chatbot process starts. Do not reload the
1.35 GB checkpoint for every message.

```python
from mercury import MercuryPredictor

mercury = MercuryPredictor(device="auto")

def classify_user_message(message: str) -> dict:
    return mercury.predict(message)
```

The result contains `label`, `confidence`, and probabilities for depression,
anxiety, and stress. Treat these as dataset-category scores, not diagnoses.
The chatbot should never state that a user has a mental-health condition.

Recommended behavior:

- Use MERCURY only as one contextual signal for response routing.
- Do not refuse supportive conversation because confidence is low.
- Do not use its label for emergency or suicide-risk decisions; this model was
  not trained or validated for crisis detection.
- Use a separate, reviewed safety flow for self-harm or imminent-danger text.
- Avoid storing raw messages unless the user has consented and retention is documented.
- Show a non-diagnostic disclaimer wherever results are exposed.
- Consider an uncertainty threshold, but calibrate it on representative data first.

HTTP option:

```powershell
python -m uvicorn api:app --host 127.0.0.1 --port 8000
```

Then POST JSON such as `{"text":"I feel overwhelmed by deadlines"}` to `/predict`.
