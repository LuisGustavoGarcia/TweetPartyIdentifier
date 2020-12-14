import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # Parse the data stored in csv format so we don't need to make calls to the
    # twitter API every time.
    csv_filepath = './Generated Data/CombinedWordFrequency.csv'
    data_frame = pd.read_csv(csv_filepath, na_filter = False)

    democrat_word_frequency = data_frame['Democrat Frequency']
    republican_word_frequency = data_frame['Republican Frequency']

    # Create Pandas DataFrame for holding data to be plotted.
    df = pd.DataFrame([democrat_word_frequency, republican_word_frequency]).transpose()
    df.columns = ['x', 'y']

    # Create scatter plot of the data points.
    class_ax = df.plot.scatter(x='x', y='y', color='Orange');
    plt.title("Frequency of Word Use By Each Party")
    plt.xlabel("Times Word Used By Democrats")
    plt.ylabel("Times Word Used By Republicans")
    
    
    # Calculate the Least Squares Decision Boundary
    m = len(democrat_word_frequency)
    # Add column of ones to account for bias term.
    X = np.array([np.ones(m), democrat_word_frequency]).transpose()
    Y = np.array([republican_word_frequency]).transpose()

    beta = np.linalg.inv(X.transpose() @ X) @ (X.T @ Y)

    # Plot the decision boundary used to decide between Democrat & Republican words.
    line_x = np.linspace(0,max(democrat_word_frequency))
    line_y = beta[0] + beta[1] * line_x
    class_ax.plot(line_x, line_y)

    # Store Results.
    plt.savefig('./Generated Figures/word_party_affilitation_scatter_plot')
    print('Figure saved to: ./Generated Figures/word_party_affilitation_scatter_plot.png')
    
    output_data = pd.DataFrame([beta[0], beta[1]]).transpose()
    output_data.columns = ['Bias','Slope']
    output_data.to_csv('./Generated Data/WordDecisionBoundary.csv',index=False)

    # Show Results.
    plt.show()
    
