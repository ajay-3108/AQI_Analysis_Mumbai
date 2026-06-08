from src.forecasting import run_sarima, run_prophet, run_lstm

import pandas as pd
df = pd.read_csv("data/processed_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")
ts = df["AQI"].asfreq("D")

# Forecast models
sarima_result = run_sarima(ts)
prophet_result = run_prophet(ts)
lstm_result = run_lstm(ts)
