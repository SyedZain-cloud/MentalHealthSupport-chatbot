import pandas as pd
import random

data = pd.read_csv("mental_health_chatbot_responses.csv")

negative_responses = data[data["intent"] == "negative"]

response = random.choice(negative_responses["response"].tolist())

print(response)