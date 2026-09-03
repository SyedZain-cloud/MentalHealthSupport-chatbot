def sentiment_analysis(text):

    positive_words = ["happy", "good", "great", "excited", "love", "like",
                      "amazing", "proud", "joy", "fun"]

    negative_words = ["sad", "bad", "stressed", "angry", "lonely",
                      "anxious", "terrible", "worried", "upset"]

    text = text.lower()

    words = text.split()

    for i in range(len(words)):

        print(i, words[i])

        word = words[i]

        if word in positive_words:

            if i > 0 and words[i - 1] == "not":
                return "negative"

            return "positive"

        if word in negative_words:

            if i > 0 and words[i - 1] == "not":
                return "positive"

            return "negative"

    return "neutral"