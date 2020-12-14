import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

if __name__ == "__main__":
    csv_filepath = './Generated Data/WordMembership.csv'
    data_frame = pd.read_csv(csv_filepath, na_filter = False)
    word_list = list(data_frame['Word'])
    weight = list(data_frame['Weight'])

    word_weight = {}
    for i in range(0, len(word_list)):
        word_weight[word_list[i]] = weight[i]

    tweet = input("Enter a tweet's text to be examined:")

    regex = re.compile('[^a-zA-Z# ]')
    words = set(regex.sub('', tweet).lower().split())

    tweet_value = 0
    for word in words:
        if word in word_list:
            tweet_value += word_weight[word]

    if tweet_value > 0:
        print("The Tweet's contents are most similar to the Republican Party's Tweets")
        return 'Republican'
    else:
        print("The Tweet's contents are most similar to the Democratic Party's Tweets")
        return 'Democrat'
