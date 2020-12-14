import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
#%matplotlib inline

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------



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



# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------


with open('x.txt', 'w') as f:
    for item in democrat_frequency_all:
        f.write("%s\n" % item)

with open('y.txt', 'w') as f:
    for item in republican_frequency_all:
        f.write("%s\n" % item)

# Read in data
x_vals = np.loadtxt('x.txt')
y_vals = np.loadtxt('y.txt')

# Throw out one data point so that there
# are an equal number from each class.
class_one = [x_vals[:], y_vals[:]]
#class_two = y_vals[:]

# Create data array for plotting
data = np.hstack((class_one))

# Create Pandas DataFrame for holding binary class data.
df = pd.DataFrame(data, columns=['x', 'y', 'dem', 'rep'])

# Create scatter plot of data points in both classes.
class_ax = df.plot.scatter(x='x', y='y', color='Orange', label='+1');
df.plot.scatter(x='dem', y='rep', color='LightBlue', label='-1', ax=class_ax);

# Create complete data array comprised
# of all points from both classes.
X = np.vstack((class_one, class_two))
m = len(X)

# Add column of ones to account for bias term
X = np.array([np.ones(m), X[:, 0], X[:, 1]]).T

# Create y array of class labels
y = np.concatenate((y_vals[51:], y_vals[:50])).T

# Calculate the Regularized Least Squares solution
beta = np.linalg.inv(X.T @ X) @ (X.T @ y)

# Create Pandas DataFrame for holding binary class data.
df = pd.DataFrame(data, columns=['x', 'y', 'x1', 'x2'])

# Create scatter plot of data points in both classes.
new_ax = df.plot.scatter(x='x', y='y', color='Orange', label='+1');
df.plot.scatter(x='x1', y='x2', color='LightBlue', label='-1', ax=new_ax);

# Plot the resulting regression line
line_x = np.linspace(0, 9)
line_y = -beta[0] / beta[2] - (beta[1] / beta[2]) * line_x

new_ax.plot(line_x, line_y)
new_ax.set_xlim((0, 9));
new_ax.set_ylim((-5, 5));
plt.show()

# Calculate the minimal RSS error
rss = np.sum((y - X @ beta) ** 2)

print("The minimum RSS error is: " + str(rss))