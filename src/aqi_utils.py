import numpy as np
import pandas as pd

breakpoints = {
    "PM2.5": [(0,30,0,50),(31,60,51,100),(61,90,101,200),(91,120,201,300),(121,250,301,400),(251,350,401,500)],
    "PM10": [(0,50,0,50),(51,100,51,100),(101,250,101,200),(251,350,201,300),(351,430,301,400),(431,600,401,500)],
    "NO2": [(0,40,0,50),(41,80,51,100),(81,180,101,200),(181,280,201,300),(281,400,301,400),(401,1000,401,500)],
    "SO2": [(0,40,0,50),(41,80,51,100),(81,380,101,200),(381,800,201,300),(801,1600,301,400),(1601,2620,401,500)],
    "CO": [(0,1,0,50),(1.1,2,51,100),(2.1,10,101,200),(10.1,17,201,300),(17.1,34,301,400),(34.1,50,401,500)],
    "Ozone": [(0,50,0,50),(51,100,51,100),(101,168,101,200),(169,208,201,300),(209,748,301,400),(749,1000,401,500)],
    "NH3": [(0,200,0,50),(201,400,51,100),(401,800,101,200),(801,1200,201,300),(1201,1800,301,400),(1801,2500,401,500)]
}

def calculate_subindex(pollutant, value):
    for (Cl, Ch, Il, Ih) in breakpoints[pollutant]:
        if Cl <= value <= Ch:
            return (Ih - Il)/(Ch - Cl) * (value - Cl) + Il
    return np.nan

def calculate_aqi(df):
    for pollutant in breakpoints:
        if pollutant in df.columns:
            df[f"{pollutant}_SI"] = df[pollutant].apply(lambda x: calculate_subindex(pollutant, x))
    df["AQI"] = df[[col for col in df.columns if col.endswith("_SI")]].max(axis=1)
    df["AQI_Category"] = df["AQI"].apply(aqi_category)
    return df

def aqi_category(aqi):
    if aqi <= 50: return "Good"
    elif aqi <= 100: return "Satisfactory"
    elif aqi <= 200: return "Moderate"
    elif aqi <= 300: return "Poor"
    elif aqi <= 400: return "Very Poor"
    else: return "Severe"
