def sentiment_analysis (text):

    positive_words = ["happy", "good", "great", "excited", "love", "like"]
    negative_words = ["sad", "bad", "stressed", "angry", "lonely"]

    text = text.lower()

    for word in positive_words:
        if word in text:
           return "positive"

    for word in negative_words:
        if word in text:
           return "negative"

    return "neutral"            