from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from mercury import MercuryPredictor

app = FastAPI(title="MERCURY Research Classifier", version="1.0.0")
predictor = MercuryPredictor()


class PredictionRequest(BaseModel):
    text: str = Field(min_length=1, max_length=10000)


@app.get("/health")
def health():
    return {"status": "ok", "device": str(predictor.device)}


@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        return predictor.predict(request.text)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
