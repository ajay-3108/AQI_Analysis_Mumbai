from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import pandas as pd

def evaluate(true, pred):
    mae = mean_absolute_error(true, pred)
    rmse = np.sqrt(mean_squared_error(true, pred))
    mape = np.mean(np.abs((true - pred) / true)) * 100
    return mae, rmse, mape

# Assume predictions and true values are loaded
# Example:
# true = ts[-90:]
# arima_pred = ...
# prophet_pred = ...
# lstm_pred = ...

results = pd.DataFrame({
    "Model": ["SARIMA", "Prophet", "LSTM"],
    "MAE": [...],
    "RMSE": [...],
    "MAPE": [...]
})

print(results)
