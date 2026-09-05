def sentiment_analysis(text):

    positive_words = [
        "happy", "good", "great", "excited", "love", "like",
        "amazing", "proud", "joy", "fun"
    ]

    negative_words = [
        "sad", "bad", "stressed", "angry", "lonely",
        "anxious", "terrible", "worried", "upset"
    ]

    negation_words = [
        "not", "don't", "never", "no"
    ]

    text = text.lower()
    words = text.split()

    for i in range(len(words)):

        word = words[i]

        recent_words = words[max(0, i - 4):i]

        is_negated = any(
            negation in recent_words
            for negation in negation_words
        )

        if word in positive_words:

            if is_negated:
                return "negative"

            return "positive"

        if word in negative_words:

            if is_negated:
                return "positive"

            return "negative"

    return "neutral"