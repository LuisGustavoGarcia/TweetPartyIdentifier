import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # Parse the data stored in csv format so we don't need to make calls to the
    # twitter API every time.
    csv_filepath = './Generated Data/WordFrequencyAndAffiliation.csv'
    word_used_data_frame = pd.read_csv(csv_filepath, na_filter = False)

    csv_filepath = './Generated Data/DemocratTweets.csv'
    democrat_tweets_data_frame = pd.read_csv(csv_filepath, na_filter = False)

    csv_filepath = './Generated Data/RepublicanTweets.csv'
    republican_tweets_data_frame = pd.read_csv(csv_filepath, na_filter = False)

    print(word_used_data_frame)
    # Todo: Decompress the csv back into a list as necessary for the equation.
