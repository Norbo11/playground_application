import pandas as pd


def load_large_csv():
    df = pd.read_csv("playground_application/large.csv")
    return df
