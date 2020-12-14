import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # Parse the data stored in csv format so we don't need to make calls to the
    # twitter API every time.
    csv_filepath = './Generated Data/WordFrequencyAndAffiliation.csv'
    word_used_data_frame = pd.read_csv(csv_filepath, na_filter = False)

    word_list = word_used_data_frame['Word']
    frequency_list = word_used_data_frame['Frequency']
    party_list = word_used_data_frame['Party Affiliation']

    democrat_word_frequencies = {}
    republican_word_frequencies = {}

    for i in range(0, len(word_list)):
        word = word_list[i]
        frequency = frequency_list[i]
        party = party_list[i]

        if party == 'Democrat':
            democrat_word_frequencies[word] = frequency
        else:
            republican_word_frequencies[word] = frequency

    # This is how we'd sort the dictionary by the frequency in Descending order.
    # sorted_democrat_words = dict(sorted(democrat_word_frequencies.items(), key=lambda item: item[1], reverse=True))

    # TODO: Plot the most said word for each party.
