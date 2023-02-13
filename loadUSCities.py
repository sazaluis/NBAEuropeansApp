import pandas as pd

def readCities():
    df = pd.read_csv("uscities.csv")

    return df