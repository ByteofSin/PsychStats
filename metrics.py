def mean(data):
    return sum(data) / len(data) if data else 0 

def mode():
    return

def median():
    return

def variance():
    sum_of_squares = sum((x - mean(data)) ** 2 for x in data)

    if len(data) > 1:
        return sum_of_squares / (len(data) - 1) 
    return 

def stddev():
    return variance() ** 0.5

def zscore():
    return (x - mean(data)) / stddev() if stddev() else 0

