import matplotlib.pyplot as plt


def histogram(data, bins=10, title='Histogram', xlabel='Value', ylabel='Frequency'):
    plt.hist(data, bins=bins, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def scatter_plot(x, y, title='Scatter Plot', xlabel='X-axis', ylabel='Y-axis'):
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def box_plot(data, title='Box Plot', xlabel='Value'):
    plt.boxplot(data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.show()  
    

    