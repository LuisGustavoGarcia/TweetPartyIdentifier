import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == "__main__":

    # Read data needed to re-draw the decision boundary.
    csv_filepath = './Generated Data/WordDecisionBoundary.csv'
    data_frame = pd.read_csv(csv_filepath, na_filter = False)
    bias = float(data_frame['Bias'])
    slope = float(data_frame['Slope'])

    # Read data neeed to plot a specific word.
    csv_filepath = './Generated Data/CombinedWordFrequency.csv'
    data_frame = pd.read_csv(csv_filepath, na_filter = False)
    word_list = list(data_frame['Word'])
    democrat_frequency_list = data_frame['Democrat Frequency']
    republican_frequency_list = data_frame['Republican Frequency']
    
    party = []
    weights = []
    for i in range(0, len(word_list)):
        word = word_list[i]
        democrat_freq = float(democrat_frequency_list[i])
        republican_freq = float(republican_frequency_list[i])

        # Check if word's frequency falls beneath the decision boundary
        line_val = bias + (slope * democrat_freq)
        if (line_val > republican_freq):
            party.append('Democrat')
            multiplier = -1
        else:
            party.append('Republican')
            multiplier = 1

        # Distance from our 'point' to the decision boundary line.
        # This will determine the influence of the word in categorizing a tweet.
        weight = ((slope * democrat_freq) + republican_freq + bias) / math.sqrt( pow(slope, 2) + pow(1, 2))
        rounded_weight = float("{:.2f}".format(weight))
        weights.append(rounded_weight * multiplier)

    output_data = pd.DataFrame([word_list, party, weights]).transpose()
    output_data.columns = ['Word','Party Affiliation', 'Weight']
    output_data.to_csv('./Generated Data/WordMembership.csv',index=False)
    print('Output written to: ./Generated Data/WordMembership.csv')
