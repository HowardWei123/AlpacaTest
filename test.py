from alpaca.data.historical import CryptoHistoricalDataClient

# No keys required for crypto data
client = CryptoHistoricalDataClient()

from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame

# Creating request object
request_params = CryptoBarsRequest(
  symbol_or_symbols=["BTC/USD"],
  timeframe=TimeFrame.Day,
  start="2024-10-03",
  end="2024-10-11"
)

# above code does not need API key
from alpaca.data import StockHistoricalDataClient, StockTradesRequest
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

alpaca_api_key = os.getenv("APCA-API-KEY-ID")
alpaca_secret_key = os.getenv("APCA-API-SECRET-KEY")

stock_hist_client = StockHistoricalDataClient(alpaca_api_key, alpaca_secret_key)

request_params = StockTradesRequest(
  symbol_or_symbols=["AAPL"],
  timeframe=TimeFrame.Day,
  start="2024-10-03",
  end="2024-10-04",
  limit=100
)

trades = stock_hist_client.get_stock_trades(request_params=request_params)

print(trades)

from alpaca.data.live import StockDataStream


stream = StockDataStream(alpaca_api_key, alpaca_secret_key)

# async handler
async def quote_data_handler(data):
    # quote data will arrive here
    print(data)

stream.subscribe_quotes(quote_data_handler, "AAPL")

stream.run()