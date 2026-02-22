from prophet import Prophet
import pandas as pd

def prophet_forecast(series):
    df = pd.DataFrame({
        "ds": pd.date_range("2023-01-01", periods=len(series), freq="M"),
        "y": series.values
    })

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=6, freq="M")
    forecast = model.predict(future)

    return forecast[["ds","yhat"]].tail(6)
