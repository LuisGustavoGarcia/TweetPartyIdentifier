import pandas as pd
import re

if __name__ == "__main__":
    csv_filepath = './Generated Data/RepublicanMemberTweets.csv'
    data_frame = pd.read_csv(csv_filepath, na_filter = False)

    # Fetch recorded tweets.
    tweets = (data_frame['Tweets'][0])

    # Remove punctuation from the tweet strings.
    regex = re.compile('[^a-zA-Z# ]')
    tweets = regex.sub('', tweets)

    # Split all the recorded tweets into their individual words.
    words_used = tweets.lower().split()

    # Read a list of non-indicative words we should ignore such as 'and' 'the' etc.
    f = open('words_to_remove.txt', 'r')
    words_to_ignore = f.readline().split(',')

    # Index the words/phrases and how often they appear in tweets.
    republican_word_frequency = {}
    for word in words_used:
        if word not in words_to_ignore:
            if (word not in republican_word_frequency):
                republican_word_frequency[word] = 1
            else:
                republican_word_frequency[word] = republican_word_frequency[word] + 1

    # Sort the words by their frequency
    sorted_frequency = sorted(republican_word_frequency.items(),key=lambda x: x[1], reverse=True)

    # Print the 50 most used phrases
    j = 0
    for i in sorted_frequency:
        print(i[0], i[1])

        j += 1
        if j == 50:
            break
