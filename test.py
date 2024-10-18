from alpaca.data.timeframe import TimeFrame
from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from alpaca.data.live import StockDataStream
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

alpaca_api_key = os.getenv("APCA-API-KEY-ID")
alpaca_secret_key = os.getenv("APCA-API-SECRET-KEY")

target_symbols = 'NVDA'

def stock_historical():
  stock_hist_client = StockHistoricalDataClient(alpaca_api_key, alpaca_secret_key)

  request_params = StockTradesRequest(
    symbol_or_symbols=target_symbols,
    timeframe=TimeFrame.Day,
    start="2024-10-17",
    end="2024-10-18",
    limit=10
  )

  trades = stock_hist_client.get_stock_trades(request_params=request_params)

  for trade in trades.data[target_symbols]:
     print(trade)
     print()


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
stock_live()