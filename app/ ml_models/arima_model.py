from statsmodels.tsa.arima.model import ARIMA

def arima_forecast(series):
    model = ARIMA(series, order=(1,1,1))
    fit = model.fit()
    return fit.forecast(steps=6)
