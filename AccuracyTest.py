import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import twitter

def find_tweets(api, handle, num_of_tweets):
    tweets = []
    try:
        timeline = api.GetUserTimeline(screen_name=handle, count=num_of_tweets, exclude_replies = True)
        for status in timeline:
            tweets.append(str(status.full_text))
    except:
        print('API Exception')
        pass
    return tweets

def avg_sum(list):
    list_sum = 0
    for i in list:
        list_sum += i

    return list_sum / len(list)

def find_accuracy_for_user(api, handle, num_of_tweets, party):
    tweets = find_tweets(api, handle, 100)
    num_correct = 0

    # Error finding tweets
    if len(tweets) == 0:
        return -1
    
    for tweet in tweets:
        regex = re.compile('[^a-zA-Z# ]')
        words = set(regex.sub('', tweet).lower().split())

        tweet_value = 0
        for word in words:
            if word in word_list:
                tweet_value += word_weight[word]

        if tweet_value < 0 and party == 'Democrat':
            num_correct += 1
        elif tweet_value > 0 and party == 'Republican':
            num_correct += 1
    return num_correct/len(tweets)

if __name__ == "__main__":
    api = twitter.Api(consumer_key='O1TcM1r6K0hKZ7bnpjslpxaG5',
                  consumer_secret='4gSL38BmKvs63PU3lucl7e4Gz60sTWPnnoxQ3IBO2vEjFxJI9U',
                  access_token_key='1331694691256070144-nks9sd74IiAyt8e4CCHktQwUNTDBor',
                  access_token_secret='iCwbCbaHfBHpJ2fs7Hov0LCGBbAQov0nEiSVbs2bgXnUV',
                    tweet_mode = 'extended')

    csv_filepath = './Generated Data/WordMembership.csv'
    data_frame = pd.read_csv(csv_filepath, na_filter = False)
    word_list = list(data_frame['Word'])
    weight = list(data_frame['Weight'])

    word_weight = {}
    for i in range(0, len(word_list)):
        word_weight[word_list[i]] = weight[i]

    csv_filepath = './Generated Data/CongressMemberTwitterHandles.csv'
    data_frame = pd.read_csv(csv_filepath, na_filter = False)
    democrat_handles = list(data_frame['Democrats'])
    republican_handles = list(data_frame['Republicans'])

    democrat_accuracy_list = []
    for handle in democrat_handles:
        accuracy = find_accuracy_for_user(api, handle, 1, 'Democrat')
        if (accuracy != -1):
            democrat_accuracy_list.append(accuracy)

    democrat_avg_accuracy = avg_sum(democrat_accuracy_list)
    print('Democrat Tweet Identification Accuracy: ' + str(float("{:.2f}".format(democrat_avg_accuracy * 100))) + '%')

    republican_accuracy_list = []
    for handle in republican_handles:
        accuracy = find_accuracy_for_user(api, handle, 1, 'Republican')
        if (accuracy != -1):
            republican_accuracy_list.append(accuracy)

    republican_avg_accuracy = avg_sum(republican_accuracy_list)
    print('Republican Tweet Identification Accuracy: ' + str(float("{:.2f}".format(republican_avg_accuracy * 100))) + '%')
    

