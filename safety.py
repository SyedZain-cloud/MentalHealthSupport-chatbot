def safety_check(text):

    crisis_words = [
        "kill myself",
        "killing myself",
        "suicide",
        "commit suicide",
        "want to die",
        "wanna die",
        "end my life",
        "ending my life",
        "hurt myself",
        "hurting myself",
        "harm myself",
        "self harm",
        "self-harm",
        "no reason to live",
        "no point in living",
        "don't want to live",
        "dont want to live",
        "not worth living",
        "better off dead"
    ]

    text = text.lower()

    for phrase in crisis_words:
        if phrase in text:
            return True

    return False