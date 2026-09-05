from mercury import MercuryPredictor


def supportive_reply(message: str, result: dict) -> str:
    # The category may guide tone, but must never be presented as a diagnosis.
    label = result["label"]
    if label == "stress":
        return "That sounds like a lot to carry. Would it help to break down what feels most urgent?"
    if label == "anxiety":
        return "It sounds like there is a lot of worry here. What feels most uncertain right now?"
    return "I’m sorry you’re having a difficult time. Would you like to tell me more about what has been hardest?"


def main():
    model = MercuryPredictor(device="auto")  # Load once, outside the chat loop.
    print("MERCURY demo. Type 'quit' to stop.")
    while True:
        message = input("You: ").strip()
        if message.lower() in {"quit", "exit"}:
            break
        result = model.predict(message)
        print("Bot:", supportive_reply(message, result))
        print("Research signal:", result["label"], f"({result['confidence']:.1%})")


if __name__ == "__main__":
    main()
