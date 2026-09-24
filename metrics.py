def mean(data, key=None):
    if key is None:
        return sum(data) / len(data)
    
    return sum(data[key]) / len(data[key]) 

def mode(data, key):
    return

def median(data, key):
    return

def variance(data, key=None):
    if key is None:
        data_values = data
    else:
        data_values = data[key]

    sum_of_squares = sum((x - mean(data_values)) ** 2 for x in data_values)

    if len(data_values) > 1:
        return sum_of_squares / (len(data_values) - 1)
    return 0

def stddev(data, key=None):
    return variance(data, key) ** 0.5

def zscore(data, x, key=None):
    if key is None:
        return (x - mean(data)) / stddev(data) if stddev(data) else 0   
    return (x - mean(data, key)) / stddev(data, key) if stddev(data, key) else 0

def skewness(data, key=None):
    if key is None:
        data_values = data
    else:
        data_values = data[key]
    n = len(data_values)
    if n < 3:
        return 0
    mean_value = mean(data_values)
    std_dev = stddev(data_values)
    skewness_value = (n * sum((x - mean_value) ** 3 for x in data_values)) / ((n - 1) * (n - 2) * (std_dev ** 3))
    return skewness_value

def kurtosis(data, key=None):
    if key is None:
        data_values = data
    else:
        data_values = data[key]
    n = len(data_values)
    if n < 4:
        return 0
    mean_value = mean(data_values)
    std_dev = stddev(data_values)
    kurtosis_value = (n * (n + 1) * sum((x - mean_value) ** 4 for x in data_values)) / ((n - 1) * (n - 2) * (n - 3) * (std_dev ** 4)) - (3 * (n - 1) ** 2) / ((n - 2) * (n - 3))
    return kurtosis_value

