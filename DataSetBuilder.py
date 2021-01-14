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
            print('API Exception')
            pass
        return tweets

def find_word_frequency(tweets):
    # Remove punctuation from the tweet strings, and split all the recorded tweets into their individual words.
    regex = re.compile('[^a-zA-Z# ]')

    words_used = []
    for tweet in tweets:
        filtered_tweet = regex.sub('', tweet).lower().split()
        words_used.extend(filtered_tweet)

    # Read a list of non-indicative words we should ignore such as 'and' 'the' etc.
    f = open('./Generated Data/words_to_remove.txt', 'r')
    words_to_ignore = f.readline().split(',')

    # Index the words/phrases and how often they appear in tweets.
    word_frequency = {}
    for word in words_used:
        if word not in words_to_ignore:
            if (word not in word_frequency):
                word_frequency[word] = 1
            else:
                word_frequency[word] = word_frequency[word] + 1

    return word_frequency

'''
    This script will create a csv. file which will store the words found in a number of tweets
    belonging to Congress members of both the Republican and Democratic parties, the frequency
    at which the words were found, and which party the word was used by.

    The amount of tweets per congress member which are used can be altered in the variable
    'num_of_tweets'.

    Before running this script, it's important that ./Generated Data/CongressMemberTwitterHandles.csv
    is populated with the Twitter Handles of all possible Congress members.
    See: './CongressMemberAccountFinder.py'
'''
if __name__ == "__main__":
    print('Started Routine') # Added this because it can be a very a time-lengthy routine.

    api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='',
                    tweet_mode = 'extended')
    
    # Find List of Democratic Congress Member's Twitter Handles.
    democrat_twitter_handles = find_twitter_handles('Democrats')

    # Find List of Republican Congress Member's Twitter Handles.
    republican_twitter_handles = find_twitter_handles('Republicans')

    # Number of tweets per member which should be analyzed
    num_of_tweets = 100

    # Find & store Democrat Member's Tweets
    democrat_tweets = []
    for handle in democrat_twitter_handles:
        democrat_tweets.extend(find_tweets(api, handle, num_of_tweets))

    output_data = pd.DataFrame([democrat_tweets]).transpose()
    output_data.columns = ['Tweet']
    output_data.to_csv('./Generated Data/DemocratTweets.csv',index=False)
        
    # Find & store Republican Member's Tweets
    republican_tweets = []
    for handle in republican_twitter_handles:
        republican_tweets.extend(find_tweets(api, handle, num_of_tweets))

    output_data = pd.DataFrame([republican_tweets]).transpose()
    output_data.columns = ['Tweet']
    output_data.to_csv('./Generated Data/RepublicanTweets.csv',index=False)
    
    # Find Democrat's word frequency
    democrat_word_frequency = find_word_frequency(democrat_tweets)

    # Find Republican's word frequency
    republican_word_frequency = find_word_frequency(republican_tweets)

    # Remove words that only occur once, these are outliers.
    # This should only be enabled if the number of tweets you are examining is very large
    # otherwise, you might potentially delete your entire dataset.
    democrat_words_to_remove = []
    republican_words_to_remove = []
    for key in democrat_word_frequency.keys():
        if democrat_word_frequency[key] == 1:
            democrat_words_to_remove.append(key)
    for key in republican_word_frequency.keys():
        if republican_word_frequency[key] == 1:
            republican_words_to_remove.append(key)

    for key in democrat_words_to_remove:
        del democrat_word_frequency[key]
    for key in republican_words_to_remove:
        del republican_word_frequency[key]

    # Combine the frequencies into a single list.
    republican_words = list(republican_word_frequency.keys())
    democrat_words = list(democrat_word_frequency.keys())
    print(republican_words)
    print(democrat_words)
    democrat_words.extend(republican_words)
    word_list = set(democrat_words)
    democrat_frequency_all = []
    republican_frequency_all = []
    for word in word_list:
        if word in democrat_word_frequency.keys():
            democrat_frequency_all.append(democrat_word_frequency[word])
        else:
            democrat_frequency_all.append(0)

        if word in republican_word_frequency.keys():
            republican_frequency_all.append(republican_word_frequency[word])
        else:
            republican_frequency_all.append(0)

    output_data = pd.DataFrame([list(word_list), democrat_frequency_all, republican_frequency_all]).transpose()
    output_data.columns = ['Word','Democrat Frequency', 'Republican Frequency']
    output_data.to_csv('./Generated Data/CombinedWordFrequency.csv',index=False)
    
    print('Finished Routine')

    
