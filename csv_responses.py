import pandas as pd
import random

data = pd.read_csv("mental_health_chatbot_responses.csv")


def get_response(intent):
    matching_rows = data[data["intent"] == intent]

    if matching_rows.empty:
        return "I'm listening. Tell me more about what's going on."

    return random.choice(matching_rows["response"].tolist())