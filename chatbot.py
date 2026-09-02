import random
from sentiment import sentiment_analysis
from responses import responses


def get_response(user_message):

    sentiment = sentiment_analysis(user_message)

    # print("Sentiment:", repr(sentiment))
    # print("Keys:", responses.keys())
    # return responses[sentiment][0]
    return random.choice(responses[sentiment])

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

    response = get_response(user_message)

    print("Mr.Bot:", response)