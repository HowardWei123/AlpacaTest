from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.data import StockHistoricalDataClient, StockBarsRequest
from alpaca.data.live import StockDataStream

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

alpaca_api_key = os.getenv("APCA-API-KEY-ID")
alpaca_secret_key = os.getenv("APCA-API-SECRET-KEY")

target_symbols = ['NVDA', 'AAPL', 'SPY']

def stock_historical():
  stock_hist_client = StockHistoricalDataClient(alpaca_api_key, alpaca_secret_key)

  request_params = StockBarsRequest(
    symbol_or_symbols=target_symbols,
    timeframe=TimeFrame(1, TimeFrameUnit.Day),
    start="2024-09-19",
    end="2024-10-19",
  )

  trades = stock_hist_client.get_stock_bars(request_params=request_params)

  # Iterate through the symbols and their respective data
  for symbol in trades.data.keys():
      print(f"Data for {symbol}:")
      for bar in trades.data[symbol]:
          print(bar)
          print()
      print()  # For better readability between symbols


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