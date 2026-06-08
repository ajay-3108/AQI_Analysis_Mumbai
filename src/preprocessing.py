import pandas as pd

def load_and_clean(path):
    df = pd.read_csv(path)
    df["From Date"] = pd.to_datetime(df["From Date"], errors="coerce")
    df["Date"] = df["From Date"].dt.date
    return df
