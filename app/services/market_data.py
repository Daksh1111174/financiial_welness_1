import yfinance as yf

def get_stock(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period="6mo")
