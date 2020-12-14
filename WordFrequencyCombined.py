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

    # Do not include a frequency of zero.
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

    # Can include a frequency of zero.
    democrat_frequency_all = []
    republican_frequency_all = []
    for word in word_list:
        if word in democrat_word_frequencies.keys():
            democrat_frequency_all.append(democrat_word_frequencies[word])
        else:
            democrat_frequency_all.append(0)

        if word in republican_word_frequencies.keys():
            republican_frequency_all.append(republican_word_frequencies[word])
        else:
            republican_frequency_all.append(0)

    output_data = pd.DataFrame([word_list.tolist(), democrat_frequency_all, republican_frequency_all]).transpose()
    output_data.columns = ['Word','Democrat Frequency', 'Republican Frequency']
    output_data.to_csv('./Generated Data/CombinedWordFrequency.csv',index=False)
