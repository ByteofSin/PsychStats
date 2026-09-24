import matplotlib.pyplot as plt
import seaborn as sns


def histogram(data, bins=10, key=None):
    if key is None:
        data_values = data
    else:
        data_values = data[key]

    sns.histplot(data_values, bins=bins, kde=True, color='blue', alpha=0.5)
    
    
    plt.title(f"{key} Histogram" if key is not None else "Histogram")
    plt.xlabel(key if key is not None else "Value")
    plt.ylabel("Frequency")

    plt.show()

def hexbin():
    return


def scatter_plot(data, xlabel='X-axis', ylabel='Y-axis'):
    plt.scatter(data[xlabel], data[ylabel])
    plt.title(f"{xlabel} vs {ylabel}")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def box_plot(data, title='Box Plot', xlabel='Value'):
    plt.boxplot(data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.show()  
    

def correlation_matrix(data):
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()

