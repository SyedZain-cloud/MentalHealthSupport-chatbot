import math

from mercury import MercuryPredictor


predictor = MercuryPredictor(device="cpu")
result = predictor.predict("I feel overwhelmed and tense because of work deadlines.")
assert result["label"] in {"depression", "anxiety", "stress"}
assert math.isclose(sum(result["probabilities"].values()), 1.0, abs_tol=1e-5)
print(result)
