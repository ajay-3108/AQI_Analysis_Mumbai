import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv("data/processed_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

ts = df["AQI"].asfreq("D")

# Plot time series
ts.plot(figsize=(12,5), title="AQI Time Series")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.show()

# Seasonal decomposition
decomp = seasonal_decompose(ts, model="additive", period=7)
decomp.plot()
plt.show()

# ACF and PACF
plot_acf(ts.dropna(), lags=50)
plt.show()
plot_pacf(ts.dropna(), lags=50)
plt.show()
