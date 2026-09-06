# import sys
# # import random
# sys.path.append("mercury_model")
# from mercury import MercuryPredictor

# from sentiment import sentiment_analysis
# from csv_responses import get_response
# # from responses import responses
# from safety import safety_check

# mercury = MercuryPredictor(device="auto")


# def mercury_response(result):

#     label = result["label"]
#     confidence = result["confidence"]


#     if confidence < 0.60:

#         print("MERCURY classification: UNCERTAIN")
#         print("Top prediction:", label)
#         print("Confidence:", f"{confidence:.2%}")

#         return get_response("uncertain")

#         # return random.choice(responses["uncertain"])

#     #print(label)
#     # print("Sentiment:", repr(sentiment))
#     # print("Keys:", responses.keys())
#     # return responses[sentiment][0]

#     print("MERCURY classification:", label)
#     print("Confidence:", f"{confidence:.2%}")

#     return get_response (label)

#     # print(sentiment)

#     # if sentiment == "positive":
#     #    return "I'm glad to hear that buddy, sounds nice... tell more!!"

#     # elif sentiment == "negative":
#     #      return "I'm so sorry bruh, you can talk with me why you feel this way"

#     # else:
#     #     return "I'm listening to you fella, tell me more"
# last_intent = None
# followup_words = [
#     "exam",
#     "exams",
#     "university",
#     "study",
#     "studies",
#     "assignment",
#     "work",
#     "family",
#     "money",
#     "relationship", 
#     "prepared",
#     "preparing",
#     "ready"
# ]

# while True:

#     user_message = input("YOU: ")
     

#     if user_message.lower() == "exit":
#         print("Mr.Bot: Sayonara!!")
#         break
#     if safety_check(user_message):
#         print("Mr.Bot: I'm really sorry you're going through this. You don't have to face this alone. Please reach out to someone you trust or contact local emergency/crisis support if you may be in immediate danger.")
#         continue    
    
#     sentiment = sentiment_analysis(user_message)
#     print ("Sentiment:", sentiment)
#     # result = mercury.predict(user_message)
#     if sentiment == "positive":
#         last_intent ="positive"
#         response = get_response("positive")
#     # print (result)

#     elif sentiment == "neutral":
#         last_intent = None
#         response = get_response("neutral")
    
    
#     elif last_intent is not None and any(
#         word in user_message.lower().split()
#         for word in followup_words

#     ):

#         response = get_response("followup")
    
        
#     else:
#         result = mercury.predict(user_message)
#         last_intent = result["label"] 
#         response = mercury_response(result)

#     print("Mr.Bot:", response)


import sys

# import random

sys.path.append("mercury_model")

from mercury import MercuryPredictor

from sentiment import sentiment_analysis

from csv_responses import get_response

# from responses import responses

from safety import safety_check

mercury = MercuryPredictor(device="auto")


def mercury_response(result):

    label = result["label"]

    confidence = result["confidence"]

    if confidence < 0.60:

        print("MERCURY classification: UNCERTAIN")

        print("Top prediction:", label)

        print("Confidence:", f"{confidence:.2%}")

        return get_response("uncertain")

        # return random.choice(responses["uncertain"])

    #print(label)

    # print("Sentiment:", repr(sentiment))

    # print("Keys:", responses.keys())

    # return responses[sentiment][0]

    print("MERCURY classification:", label)

    print("Confidence:", f"{confidence:.2%}")

    return get_response(label)

    # print(sentiment)

    # if sentiment == "positive":

    #    return "I'm glad to hear that buddy, sounds nice... tell more!!"

    # elif sentiment == "negative":

    #      return "I'm so sorry bruh, you can talk with me why you feel this way"

    # else:

    #     return "I'm listening to you fella, tell me more"


last_intent = None


followup_words = [

    "exam",

    "exams",

    "university",

    "study",

    "studies",

    "assignment",

    "work",

    "family",

    "money",

    "relationship",

    "prepared",

    "preparing",

    "ready"

]


while True:

    user_message = input("YOU: ")

    if user_message.lower() == "exit":

        print("Mr.Bot: Sayonara!!")

        break


    if safety_check(user_message):

        print("Mr.Bot: I'm really sorry you're going through this. You don't have to face this alone. Please reach out to someone you trust or contact local emergency/crisis support if you may be in immediate danger.")

        continue


    sentiment = sentiment_analysis(user_message)

    print("Sentiment:", sentiment)

    # result = mercury.predict(user_message)


    if sentiment == "positive":

        last_intent = "positive"

        response = get_response("positive")


    # print (result)

    elif last_intent is not None and any(

        word in user_message.lower().split()

        for word in followup_words

    ):

        response = get_response("followup")


    elif sentiment == "neutral":

        last_intent = None

        response = get_response("neutral")


    else:

        result = mercury.predict(user_message)

        last_intent = result["label"]

        response = mercury_response(result)


    print("Mr.Bot:", response)

