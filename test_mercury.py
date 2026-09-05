import sys
sys.path.append("mercury_model")
from mercury import MercuryPredictor

mercury = MercuryPredictor(device="auto")

# result = mercury.predict("I feel overwhelmed with everything")
message = input("Enter a message: ")
result = mercury.predict(message)

print(result)