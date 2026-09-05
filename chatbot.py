import sys
import random
sys.path.append("mercury_model")
from mercury import MercuryPredictor

from sentiment import sentiment_analysis
from responses import responses
from safety import safety_check

mercury = MercuryPredictor(device="auto")


def get_response(result):

    label = result["label"]
    confidence = result["confidence"]


    if confidence < 0.60:

        print("MERCURY classification: UNCERTAIN")
        print("Top prediction:", label)
        print("Confidence:", f"{confidence:.2%}")

        return random.choice(responses["uncertain"])

    #print(label)
    # print("Sentiment:", repr(sentiment))
    # print("Keys:", responses.keys())
    # return responses[sentiment][0]

    print("MERCURY classification:", label)
    print("Confidence:", f"{confidence:.2%}")

    return random.choice(responses[label])

    # print(sentiment)

    # if sentiment == "positive":
    #    return "I'm glad to hear that buddy, sounds nice... tell more!!"

    # elif sentiment == "negative":
    #      return "I'm so sorry bruh, you can talk with me why you feel this way"

    # else:
    #     return "I'm listening to you fella, tell me more"

while True:

    user_message = input("YOU: ")
     

    if user_message.lower() == "exit":
        print("Mr.Bot: Sayonara!!")
        break
    if safety_check(user_message):
        print("Mr.Bot: I'm really sorry you're going through this. You don't have to face this alone. Please reach out to someone you trust or contact local emergency/crisis support if you may be in immediate danger.")
        continue    
    
    sentiment = sentiment_analysis(user_message)
    print ("Sentiment:", sentiment)
    result = mercury.predict(user_message)
    if sentiment == "positive":
        response = random.choice(responses["positive"])
    # print (result)

    else:
        result = mercury.predict(user_message) 
        response = get_response(result)

    print("Mr.Bot:", response)