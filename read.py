import pandas as pd


def read_file_csv(uri):
    data = pd.read_csv(uri, skipfooter=1)
    return data
