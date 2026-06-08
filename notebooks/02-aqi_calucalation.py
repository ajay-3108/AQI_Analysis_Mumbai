import pandas as pd
import numpy as np
from src.aqi_utils import calculate_aqi, aqi_category

# Load combined data
df = pd.read_csv("data/processed/combined_raw.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Daily averages per station
daily_df = df.groupby(["Source", "Date"])[["PM2.5", "PM10", "NO2", "SO2", "CO", "Ozone", "NH3"]].mean().reset_index()

# National average (optional)
national_df = df.groupby(["Date"])[["PM2.5", "PM10", "NO2", "SO2", "CO", "Ozone", "NH3"]].mean().reset_index()
national_df["Date"] = pd.to_datetime(national_df["Date"])
final_df = national_df[national_df["Date"] <= pd.to_datetime("2023-01-31")]

# AQI Calculation
aqi_df = calculate_aqi(final_df)
aqi_df.to_csv("data/processed_data.csv", index=False)
