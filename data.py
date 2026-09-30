import pandas as pd
import numpy as np
import pyspssio

def import_data(file_path:str):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".sav"):
        return pyspssio.read_sav(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")

def get_stats(data:pd.DataFrame, key=None, print_metrics=False):
    if key is None:
        desc = {}

        for column in data.columns:
            desc[column] = get_descriptive_stats(data, column)
    else:
        desc = {
            key: get_descriptive_stats(data, key)
        }


    if print_metrics == True:
        # Get metrics
        metrics = set()

        for key in data.columns:
            for metric in desc[key]:
                metrics.add(metric)
        
        # Get max length of column names
        str_length = max(len(key) for key in data.columns)

        # Print header
        print(f"{'':<{str_length}}", end="")
        
        for metric in metrics:
            print(f"| {metric:<{str_length}}", end="")


        # Print data
        for key in data.columns:
            print(f"{key:<{str_length}}", end="")
            for metric in metrics:
                if metric in desc[key]:
                    if data[key].dtype is np.float64 or data[key].dtype == np.int64:
                        pr = desc[key][metric]
                    else:
                        pr = desc[key][metric]
                else:
                    pr = "NA"

                print(f"| {pr}", end="")    
            print()


    return desc

def get_descriptive_stats(data:pd.DataFrame, key:str):


    desc = {}

    if data[key].dtype == "float64" or data[key].dtype == "int64":
        desc["mean"] = data[key].mean()
        desc["median"] = data[key].median()
        desc["mode"] = data[key].mode()
        desc["std"] = data[key].std()
        desc["min"] = data[key].min()
        desc["max"] = data[key].max()
        desc["range"] = data[key].max() - data[key].min()
        desc["variance"] = data[key].var()
        desc["skewness"] = data[key].skew()
        desc["kurtosis"] = data[key].kurt()
    else:
        desc["mode"] = data[key].mode()
        desc["count"] = data[key].count()
        desc["unique"] = data[key].unique()
        desc["top"] = data[key].value_counts().index[0]
        desc["freq"] = data[key].value_counts().iloc[0]


    return desc


# Data Manipulation
def add_column(data:pd.DataFrame, column:str, values:list):
    data[column] = values
    return data

def remove_column(data:pd.DataFrame, column:str):
    data.drop(columns=[column], inplace=True)
    return data

def rename_column(data:pd.DataFrame, old_name:str, new_name:str):
    data.rename(columns={old_name: new_name}, inplace=True)
    return data

def reorder_columns(data:pd.DataFrame, columns:list):
    data = data[columns]
    return data

def set_column_dtype(data:pd.DataFrame, column:str, dtype:np.dtype):
    data[column] = data[column].astype(dtype)
    return data

def set_index(data:pd.DataFrame, column:str, index:int, value:any):
    data.loc[index, column] = value
    return data

def add_row(data:pd.DataFrame, row:list):
    data.loc[len(data)] = row
    return data

def remove_row(data:pd.DataFrame, index:int):
    data.drop(index=index, inplace=True)
    return data

def rename_row(data:pd.DataFrame, old_name:str, new_name:str):
    data.rename(index={old_name: new_name}, inplace=True)
    return data

def one_hot_encode(data:pd.DataFrame, column:str):
    data = pd.get_dummies(data, columns=[column])
    return data

def label_encode(data:pd.DataFrame, column:str):
    data[column] = data[column].astype("category")
    data[column] = data[column].cat.codes
    return data

def one_hot_decode(data:pd.DataFrame, column:str):
    data[column] = data[column].astype("category")
    data[column] = data[column].cat.codes
    return data

def reverse_code(data:pd.DataFrame, column:str, inplace:bool=False, add_col:bool = False):
    reverse_data = data[column].max() - data[column]
    
    if inplace:
        data[column] = reverse_data
    elif add_col == True:
        add_column(data, f"{column}_reverse", reverse_data)

    return reverse_data