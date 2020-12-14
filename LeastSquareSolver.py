import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
    The goal is for f(x) = Likelyhood of being Democrat/Republican.
    i.e f(x) > 0 => a tweet's contents likely represent Democratic view points
    i.e f(x) < 0 => a tweet's contents likely represent Republican view points

    Want to use the formula f(x) = ax1 + bx2 + cx3 + ... nxn + c
    where xn is how many times a specific word appeared, and a is
    the coefficient which determines that word's weight in influencing the
    political inclination of a tweet.
    c is the y-intercept.

    After we find all of our constants, we can graph f(x) by inputting all of the
    words we have collected from the tweets.
    
    When graphing f(x) the 'best fit' line represents our borderline.
    i.e if something is above the line, it is of one political inclination
    if it is below, it is of another.

    This is how you create a matrix using numpy. This matrix is a 3x2 matrix.
    This means we examined 3 tweets, and the 3 tweets only ever used 2 distinct words.
    x = np.array([
    [2, 1],
    [0, 4],
    [3, 2]
    ])

    This would be sample values for f(x) where we have assigned 2 democrat tweets
    and 1 republican tweet.
    f = np.array([[1], [-1], [1]])

    Solve using least squares library
    We can understand this as being Ax = b, except it is xa = f(x)
    a = np.linalg.lstsq(x, f, rcond = None)

    Then, we would need to graph this for demonstration purposes
    And make it possible to input a tweet manually to be analyzed as belonging
    to one party or another.(aka get its F(x) value)
'''

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
