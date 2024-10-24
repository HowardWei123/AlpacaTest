from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.data import StockHistoricalDataClient, StockBarsRequest
from alpaca.data.live import StockDataStream

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

alpaca_api_key = os.getenv("APCA-API-KEY-ID")
alpaca_secret_key = os.getenv("APCA-API-SECRET-KEY")

target_symbols = ['AAPL', 'ABNB', 'AMD', 'AMC', 'BRK.B', 'BND', 'BEP', 'DIS', 'GME', 'GOOG', 'KO', 'MSFT', 'NEE', 'NVDA', 'PG', 'PLTR', 'SPY', 'TSLA', 'UL', 'V', 'VTI', 'WMT', 'BSV', 'IWM', 'ZM']


def stock_historical():
  stock_hist_client = StockHistoricalDataClient(alpaca_api_key, alpaca_secret_key)

  request_params = StockBarsRequest(
    symbol_or_symbols=target_symbols,
    timeframe=TimeFrame(1, TimeFrameUnit.Day),
    start="2024-09-20",
  )

  trades = stock_hist_client.get_stock_bars(request_params=request_params)

  # Open the output file in write mode
  with open('output.txt', 'w') as f:
      # Sort the keys of trades.data
        sorted_symbols = sorted(trades.data.keys())
        
        # Iterate through the sorted symbols and their respective data
        for symbol in sorted_symbols:
            f.write(f"Data for {symbol}:\n")  # Write the symbol to the file
            for bar in trades.data[symbol]:
                f.write(f"{bar}\n")  # Write each bar to the file
            f.write("\n")  # For better readability between symbols


def stock_live():
  stream = StockDataStream(alpaca_api_key, alpaca_secret_key)

  # async handler
  async def quote_data_handler(data):
      # quote data will arrive here
      print(data)
      print()

  stream.subscribe_quotes(quote_data_handler, target_symbols)

  stream.run()

stock_historical()