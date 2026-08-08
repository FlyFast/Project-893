import requests
import time

# Create a function to get the RSI value for a given stock symbol
def get_rsi(symbol, API_KEY):
    resp = requests.get(
        'https://v2.taapi.io/indicator/rsi',
        headers={'Authorization': 'Bearer ' + API_KEY},
        params={'exchange': 'stocks', 'symbol': symbol, 'timeframe': '1d', 'period': 14,} )
    return resp.json()

# Symbols for RSI values
symbols = [
    'AMZN', 'MSFT', 'GOOG', 'GEV', 'AAPL', 'AA', 'XOM', 'RIO', 'APD', 'PBF',
    'ETN', 'LIN', 'EQNR', 'CVX', 'BKR', 'VLO', 'VG', 'CF', 'LYB', 'DOW', 'NTR', 
    'TPL', 'COHR', 'AAOI', 'IREN', 'MP', 'LITE', 'GLW', 'MTZ', 'MKSI', 'FSLR', 
    'KLAC', 'CIEN', 'STRL', 'AVGO', 'MU', 'JBL', 'FIX', 'ECG']

# Get the api key from the API.KEY file
with open('API.KEY', 'r') as f:
    API_KEY = f.read().strip()  

# For each symbol in the list, get the RSI value and print it
for symbol in symbols:
    resp = get_rsi(symbol, API_KEY)
    print(f"{symbol}: {resp}")

    # Add a 15 second delay before making the next request
    time.sleep(15)

print("All RSI values have been retrieved.")

