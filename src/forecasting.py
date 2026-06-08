import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from prophet import Prophet
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def run_sarima(ts):
    model = SARIMAX(ts, order=(1,1,1), seasonal_order=(1,1,1,7))
    result = model.fit(disp=False)
    return result.forecast(90)

def run_prophet(ts):
    df = ts.reset_index().rename(columns={"Date":"ds", "AQI":"y"})
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=90)
    forecast = model.predict(future)
    return forecast[["ds", "yhat"]].tail(90)

def run_lstm(ts):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(ts.values.reshape(-1, 1))
    X, y = [], []
    for i in range(60, len(scaled)):
        X.append(scaled[i-60:i])
        y.append(scaled[i])
    X, y = np.array(X), np.array(y)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1],1)))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(optimizer="adam", loss="mse")
    model.fit(X, y, epochs=10, batch_size=32)

    last_60 = scaled[-60:]
    forecast = []
    input_seq = last_60
    for _ in range(90):
        input_seq_reshaped = input_seq.reshape(1, 60, 1)
        pred = model.predict(input_seq_reshaped, verbose=0)
        forecast.append(pred[0,0])
        input_seq = np.append(input_seq[1:], pred, axis=0)
    
    return scaler.inverse_transform(np.array(forecast).reshape(-1,1)).flatten()
