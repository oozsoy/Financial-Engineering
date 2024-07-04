import yfinance as yf
import os 

symbols = ['MMM', 'ABT', 'ABBV', 'ACN', 'ATVI', 'ADBE', 'AMD', 'AAP', 'AES',
  'AFL', 'AKAM', 'IBM', 'GOOG', 'SBUX', 'AAPL', 'SPY', 'NVDA', 'BNTX'] # including Biontech `BNTX` which is not in SP500 index 

# As for SPY, it is the ticker symbol for the SPDR S&P 500 ETF Trust, which is an exchange-traded fund (ETF) that tracks the S&P 500 index.

symbols.append('SPL')

if not os.path.exists('data'):
    os.mkdir('data')
    
for symbol in symbols:
    if not os.path.exists(f"data/{symbol}.csv"):
        data = yf.download(symbol, start = '2013-01-01', end = '2021-12-31')
        if data.size > 0:
            data.to_csv(f"data/{symbol}.csv")
        else:
            print(f"Issue with saving data for {symbol}")
            
for symbol in symbols:
    
    s = open(f"data/{symbol}.csv").readlines()
    if len(s) < 500: # if any of the data we saved has less than 100 lines 
        os.system(f"rm data/{symbol}.csv")

