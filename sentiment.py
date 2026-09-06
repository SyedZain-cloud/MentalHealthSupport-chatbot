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

    loss_words = [
        "anymore",
        "no longer"
    ]


    text = text.lower()

    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("!", "")
    text = text.replace("?", "")

    words = text.split()

    loss_patterns = [
        "don't feel",
        "dont feel",
        "no longer feel",
        "can't feel",
        "cannot feel"
    ]

    avoidance_patterns = [
        "don't want to",
        "dont want to",
        "no longer want to",
        "do not want to"
    ]  

    change_patterns = [
       "used to",
       "but now",
       "before",
       "now"
    ]

    for pattern in loss_patterns:
        if pattern in text:
            for word in positive_words:
                if word in words:
                    if any( loss in text for loss in loss_words):
                        return "negative"

    for pattern in avoidance_patterns:
        if pattern in text:
            return "neutral"   

    for pattern in change_patterns:
        if pattern in text:
            if "but now" in text:
                current_part = text.split("but now", 1)[1]

            elif "now" in text:
                current_part = text.split("now", 1)[1]      

            else:
                continue  

            current_words = current_part.split() 
            print("CURRENT PART:", current_part)
            print("CURRENT WORDS:", current_words)
            
            for word in current_words:
                if word in positive_words:
                    return "positive"

                if word in negative_words:
                    return "negative" 

                    

                        
                                                                
       

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