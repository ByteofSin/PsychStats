import matplotlib.pyplot as plt


def histogram(data, bins=10, title='Histogram', xlabel='Value', ylabel='Frequency'):
    plt.hist(data, bins=bins, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

