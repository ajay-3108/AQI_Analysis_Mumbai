import pandas as pd
import kagglehub

# Download dataset
path = kagglehub.dataset_download("gyaswanth297/air-quality-indexaqi-data-of-mumbai")

# Read all station files
stations = [
    "BandraKurlaComplexMumbaiIITM", "BandraMumbaiMPCB", "BorivaliEastMumbaiIITM",
    "BorivaliEastMumbaiMPCB", "ChakalaAndheriEastMumbaiIITM",
    "ChhatrapatiShivajiIntlAirportT2MumbaiMPCB", "ColabaMumbaiMPCB",
    "DeonarMumbaiIITM", "KandivaliEastMumbaiMPCB", "KhindipadaBhandupWestMumbaiIITM",
    "KurlaMumbaiMPCB", "MaladWestMumbaiIITM", "MazgaonMumbaiIITM", "MulundWestMumbaiMPCB",
    "NavyNagarColabaMumbaiIITM", "PowaiMumbaiMPCB", "SiddharthNagarWorliMumbaiIITM",
    "SionMumbaiMPCB", "VasaiWestMumbaiMPCB", "VileParleWestMumbaiMPCB", "WorliMumbaiMPCB"
]

dfs = []
for name in stations:
    df = pd.read_csv(path + f"/{name}.csv")
    df["Source"] = name
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

# Convert dates
combined_df["From Date"] = pd.to_datetime(combined_df["From Date"], errors="coerce")
combined_df["To Date"] = pd.to_datetime(combined_df["To Date"], errors="coerce")
combined_df["Datetime"] = combined_df["From Date"]
combined_df["Date"] = combined_df["Datetime"].dt.date

# Keep only numeric pollutants
pollutant_cols = ["PM2.5", "PM10", "NO2", "SO2", "CO", "Ozone", "NH3"]
for col in pollutant_cols:
    if col in combined_df.columns:
        combined_df[col] = pd.to_numeric(combined_df[col], errors="coerce")

combined_df.to_csv("data/processed/combined_raw.csv", index=False)
