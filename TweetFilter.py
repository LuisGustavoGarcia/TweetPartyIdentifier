import numpy as np
import pandas as pd
import re
import twitter

def find_twitter_handles(party):
    csv_filepath = './Generated Data/CongressMemberTwitterHandles.csv'
    data_frame = pd.read_csv(csv_filepath, na_filter = False)
    twitter_handles = []
    for handle in data_frame[party]:
        if handle != '':
            twitter_handles.append(handle)
    return twitter_handles

def find_tweets(api, handle, num_of_tweets):
        tweets = []
        try:
            timeline = api.GetUserTimeline(screen_name=handle, count=num_of_tweets, exclude_replies = True)
            for status in timeline:
                tweets.append(str(status.full_text))
        except:
            pass
        return tweets

def find_word_frequency(tweets):
    # Remove punctuation from the tweet strings, and split all the recorded tweets into their individual words.
    regex = re.compile('[^a-zA-Z# ]')

    words_used = []
    for tweet in tweets:
        filtered_tweet = regex.sub('', tweet).lower().split()
        words_used.extend(filtered_tweet)

    words_set = set(words_used)

    # Read a list of non-indicative words we should ignore such as 'and' 'the' etc.
    f = open('./Generated Data/words_to_remove.txt', 'r')
    words_to_ignore = f.readline().split(',')

    # Index the words/phrases and how often they appear in tweets.
    word_frequency = {}
    for word in words_set:
        if word not in words_to_ignore:
            if (word not in word_frequency):
                word_frequency[word] = 1
            else:
                word_frequency[word] = word_frequency[word] + 1

    return word_frequency

if __name__ == "__main__":
    api = twitter.Api(consumer_key='O1TcM1r6K0hKZ7bnpjslpxaG5',
                  consumer_secret='4gSL38BmKvs63PU3lucl7e4Gz60sTWPnnoxQ3IBO2vEjFxJI9U',
                  access_token_key='1331694691256070144-nks9sd74IiAyt8e4CCHktQwUNTDBor',
                  access_token_secret='iCwbCbaHfBHpJ2fs7Hov0LCGBbAQov0nEiSVbs2bgXnUV',
                    tweet_mode = 'extended')
    
    # Find List of Democratic Congress Member's Twitter Handles.
    democrat_twitter_handles = find_twitter_handles('Democrats')

    # Find List of Republican Congress Member's Twitter Handles.
    republican_twitter_handles = find_twitter_handles('Republicans')

    # Find Democrat Member's Tweets
    democrat_tweets = []
    num_of_tweets = 2 # Per Member
    for handle in democrat_twitter_handles:
        democrat_tweets.extend(find_tweets(api, handle, num_of_tweets))
    
    # Find Republican Member's Tweets
    republican_tweets = []
    num_of_tweets = 2 # Per Member
    for handle in republican_twitter_handles:
        republican_tweets.extend(find_tweets(api, handle, num_of_tweets))
    
    # Find Democrat's word frequency
    democrat_word_frequency = find_word_frequency(democrat_tweets)

    # Find Republican's word frequency
    republican_word_frequency = find_word_frequency(republican_tweets)

    # Create list of all words, so we can assign them an index. i.e x1 - xn
    all_words = []
    all_words.extend(democrat_word_frequency.keys())

    
