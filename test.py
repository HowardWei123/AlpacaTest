from alpaca.data.timeframe import TimeFrame, TimeFrameUnit

from alpaca.data import StockHistoricalDataClient
from alpaca.data import StockBarsRequest, StockLatestBarRequest
from alpaca.data import StockQuotesRequest, StockLatestQuoteRequest
from alpaca.data import StockTradesRequest, StockLatestTradeRequest
from alpaca.data import StockSnapshotRequest
from alpaca.data import NewsClient, NewsRequest

from alpaca.data.live import StockDataStream, NewsDataStream

import os
from dotenv import load_dotenv
from datetime import datetime

# program timer
import time
start_time = time.time()

# Load environment variables from .env file
load_dotenv()
alpaca_api_key = os.getenv("APCA-API-KEY-ID")
alpaca_secret_key = os.getenv("APCA-API-SECRET-KEY")


target_symbols = ['AAPL', 'ABNB', 'AMD', 'AMC', 'BRK.B', 'BND', 'BEP', 'DIS', 'GME',
                  'GOOG', 'KO', 'MSFT', 'NEE', 'NVDA', 'PG', 'PLTR', 'SPY', 'TSLA', 
                  'UL', 'V', 'VTI', 'WMT', 'BSV', 'IWM', 'ZM']
stock_hist_client = StockHistoricalDataClient(alpaca_api_key, alpaca_secret_key)
stream = StockDataStream(alpaca_api_key, alpaca_secret_key)


'''------------------------------------HISTORICAL INFORMATION---------------------------------'''
def write_historical_to_files(data_to_write, latest: bool, file_name: str):
    if not latest:
        data_to_write = data_to_write.data

    with open(file_name, 'w') as f:
        sorted_symbols = sorted(data_to_write.keys())
        
        for symbol in sorted_symbols:
            f.write(f"Data for {symbol}:\n")
            for data in data_to_write[symbol]:
                f.write(f"{data}\n")
            f.write("\n")


def stock_historical_bars():
    """
    Fetches historical bar data for specified stock symbols and writes it to an output file.

    This function requests historical stock bar data for a list of target symbols
    over a specified time frame and date range. The retrieved data is saved to a file
    with each symbol's data organized and separated for readability.

    PARAMETERS:
        - symbol_or_symbols (str or list of str): The target stock symbol(s) for which to fetch bar data.
        - timeframe (TimeFrame): The time interval between each bar.
            - In this case, each bar represents a 1-hour interval.
        - start (datetime): The start date and time for the historical data using datetime library.
        - end (datetime): The end date and time for the historical data using datetime library.

    STEPS:
        1. Creates a `StockBarsRequest` object with the specified symbols, timeframe, start, and end dates.
        2. Fetches the stock bars using `stock_hist_client.get_stock_bars`.
        3. Opens 'hist_bars_output.txt' in write mode.
        4. Sorts the symbols in the response data for organized output.
        5. Writes each symbol's historical bar data to the file, with each bar on a new line.

    OUTPUT:
        - A file named 'hist_bars_output.txt' with the historical bar data for each symbol.
          Each symbol's data is separated by newlines for readability.
        - Ran for 25 stocks across 20 total days and took 4.315 seconds.

    RETURNS:
        None
    """
    request_params = StockBarsRequest(
        symbol_or_symbols=target_symbols,
        timeframe=TimeFrame(2, TimeFrameUnit.Hour),
        start=datetime(2024, 9, 28),
    )

    bars = stock_hist_client.get_stock_bars(request_params=request_params)
    
    write_historical_to_files(data_to_write=bars, latest=False, file_name='hist_bars_output.txt')


def stock_historical_quotes():
    """
    Fetches historical quote data for a specified stock symbol and writes it to an output file.

    This function retrieves historical quote data for a target stock symbol over a specified
    date range. The quotes are saved to a file, with each symbol's data organized and separated
    for easy reading.

    PARAMETERS:
        - symbol_or_symbols (str): The target stock symbol for which to fetch quote data. 
            - In this example, it's set to 'AAPL' (Apple Inc.).
        - start (datetime): The start date and time for the historical data using datetime library.
        - end (datetime): The end date and time for the historical data using datetime library.

    STEPS:
        1. Creates a `StockQuotesRequest` object with the specified symbol, start, and end dates.
        2. Fetches the stock quotes using `stock_hist_client.get_stock_quotes`.
        3. Opens 'hist_quotes_output.txt' in write mode.
        4. Sorts the symbols in the response data for organized output.
        5. Writes each symbol's historical quote data to the file, with each quote on a new line.

    OUTPUT:
        - A file named 'hist_quotes_output.txt' with the historical quote data for the specified symbol.
          Each symbol's data is separated by newlines for readability.
        - Ran for 1 stock (AAPL) across 10 minutes and took 2.842 seconds.

    RETURNS:
        None
    """
    request_params = StockQuotesRequest(
        symbol_or_symbols='AAPL',
        start=datetime(2024, 10, 25, 15, 0, 0),
        end=datetime(2024, 10, 25, 15, 10, 0),
    )

    quotes = stock_hist_client.get_stock_quotes(request_params=request_params)

    write_historical_to_files(data_to_write=quotes, latest=False, file_name='hist_quotes_output.txt')


def stock_historical_trades():
    """
    Fetches historical trade data for a specified stock symbol and writes it to an output file.

    This function retrieves historical trade data for a target stock symbol over a specified
    date range, capturing trades occurring every few seconds within the day. The data is saved
    to a file, with each symbol's trades organized and separated for readability.

    PARAMETERS:
        - symbol_or_symbols (str): The target stock symbol for which to fetch trade data.
            - In this example, it's set to 'AAPL' (Apple Inc.).
        - start (datetime): The start date and time for the historical data using datetime library.
        - end (datetime): The end date and time for the historical data using datetime library.

    STEPS:
        1. Creates a `StockTradesRequest` object with the specified symbol, start, and end dates.
        2. Fetches the stock trades using `stock_hist_client.get_stock_trades`.
        3. Opens 'hist_trades_output.txt' in write mode.
        4. Sorts the symbols in the response data for organized output.
        5. Writes each symbol's historical trade data to the file, with each trade on a new line.

    OUTPUT:
        - A file named 'hist_trades_output.txt' with the historical trade data for the specified symbol.
          Each symbol's data is separated by newlines for readability.
        - Ran for 1 stock (AAPL) across 10 minutes and took 3.597 seconds.

    RETURNS:
        None
    """
    request_params = StockTradesRequest(
        symbol_or_symbols='AAPL',
        start=datetime(2024, 10, 25, 15, 0, 0),
        end=datetime(2024, 10, 25, 15, 10, 0),
    )

    trades = stock_hist_client.get_stock_trades(request_params=request_params)

    write_historical_to_files(data_to_write=trades, latest=False, file_name='hist_trades_output.txt')


def stock_historical_latest_quote():
    """
    Fetches the latest quote data for specified stock symbols and writes it to an output file.

    This function retrieves the latest stock quote for a list of target symbols and saves
    the data to a file, with each symbol's latest quote data organized and separated for readability.

    PARAMETERS:
        - symbol_or_symbols (str or list of str): The target stock symbols for which to fetch the latest quote data.
            - In this case, it's provided by the variable `target_symbols`.

    STEPS:
        1. Creates a `StockLatestQuoteRequest` object with the specified symbols.
        2. Fetches the latest stock quotes using `stock_hist_client.get_stock_latest_quote`.
        3. Opens 'latest_quote_output.txt' in write mode.
        4. Sorts the symbols in the response data for organized output.
        5. Writes each symbol's latest quote data to the file, with each quote on a new line.

    OUTPUT:
        - A file named 'latest_quote_output.txt' with the latest quote data for each symbol.
          Each symbol's data is separated by newlines for readability.
        - Ran for 25 stocks and took 0.298 seconds.

    RETURNS:
        None
    """
    request_params = StockLatestQuoteRequest(
        symbol_or_symbols=target_symbols,
    )

    quotes = stock_hist_client.get_stock_latest_quote(request_params=request_params)

    write_historical_to_files(data_to_write=quotes, latest=True, file_name='latest_quote_output.txt')


def stock_historical_latest_trade():
    """
    Fetches the latest trade data for specified stock symbols and writes it to an output file.

    This function retrieves the latest trade data for a list of target symbols and saves
    the data to a file, with each symbol's latest trade data organized and separated for readability.

    PARAMETERS:
        - symbol_or_symbols (str or list of str): The target stock symbols for which to fetch the latest trade data.
            - In this case, it's provided by the variable `target_symbols`.

    STEPS:
        1. Creates a `StockLatestTradeRequest` object with the specified symbols.
        2. Fetches the latest trade data using `stock_hist_client.get_stock_latest_trade`.
        3. Opens 'latest_trade_output.txt' in write mode.
        4. Sorts the symbols in the response data for organized output.
        5. Writes each symbol's latest trade data to the file, with each trade on a new line.

    OUTPUT:
        - A file named 'latest_trade_output.txt' with the latest trade data for each symbol.
          Each symbol's data is separated by newlines for readability.
        - Ran for 25 stocks and took 0.317 seconds.

    RETURNS:
        None
    """
    request_params = StockLatestTradeRequest(
        symbol_or_symbols=target_symbols,
    )

    trades = stock_hist_client.get_stock_latest_trade(request_params=request_params)

    write_historical_to_files(data_to_write=trades, latest=True, file_name='latest_trade_output.txt')


def stock_historical_latest_bar():
    """
    Fetches the latest bar data for specified stock symbols and writes it to an output file.

    This function retrieves the latest bar (price data for a specified time interval) for a list
    of target symbols and saves the data to a file. Each symbol's latest bar data is organized and separated
    for readability.

    PARAMETERS:
        - symbol_or_symbols (str or list of str): The target stock symbols for which to fetch the latest bar data.
            - In this case, it's provided by the variable `target_symbols`.

    STEPS:
        1. Creates a `StockLatestBarRequest` object with the specified symbols.
        2. Fetches the latest bar data using `stock_hist_client.get_stock_latest_bar`.
        3. Opens 'latest_bar_output.txt' in write mode.
        4. Sorts the symbols in the response data for organized output.
        5. Writes each symbol's latest bar data to the file, with each bar on a new line.

    OUTPUT:
        - A file named 'latest_bar_output.txt' with the latest bar data for each symbol.
          Each symbol's data is separated by newlines for readability.
        - Ran for 25 stocks and took 0.398 seconds.

    RETURNS:
        None
    """
    request_params = StockLatestBarRequest(
        symbol_or_symbols=target_symbols,
    )

    bars = stock_hist_client.get_stock_latest_bar(request_params=request_params)

    write_historical_to_files(data_to_write=bars, latest=True, file_name='latest_bar_output.txt')


def stock_historical_latest_snapshot():
    """
    Fetches the latest stock snapshots for specified symbols and writes the data to an output file.

    This function retrieves the latest stock snapshot data for a list of target symbols and saves 
    the organized data to a file. Each symbol's data is separated for improved readability.

    PARAMETERS:
        - symbol_or_symbols (str or list of str): The target stock symbols for which to fetch the 
          latest snapshot data.
          - In this case, it's provided by the variable `target_symbols`.

    STEPS:
        1. Creates a `StockSnapshotRequest` object with the specified symbols.
        2. Fetches the latest snapshot data using `stock_hist_client.get_stock_snapshot`.
        3. Opens 'latest_snapshot_output.txt' in write mode.
        4. Sorts the symbols in the response data for organized output.
        5. Writes each symbol's latest snapshot data to the file, with each entry on a new line.

    OUTPUT:
        - A file named 'latest_snapshot_output.txt' with the latest snapshot data for each symbol.
          Each symbol's data is separated by newlines for readability.
        - Ran for 25 stocks and took 0.319 seconds.

    RETURNS:
        None
"""
    request_params = StockSnapshotRequest(
        symbol_or_symbols=target_symbols,
    )

    snapshots = stock_hist_client.get_stock_snapshot(request_params=request_params)

    write_historical_to_files(data_to_write=snapshots, latest=True, file_name='latest_snapshot_output.txt')


def stock_historical_news():
    """
    Fetches historical news data for a specified stock symbol and writes it to an output file.

    This function retrieves historical news articles for a specified stock symbol ('AAPL') and saves
    the data to a file, with each article's information organized and separated for readability.

    PARAMETERS:
        - None. Uses global variables `alpaca_api_key` and `alpaca_secret_key` for authentication.

    STEPS:
        1. Creates a `NewsRequest` object with parameters for the specified stock symbol, start date, 
           exclusion of contentless articles, and a limit on the number of articles.
        2. Fetches the historical news articles using `hist_news_client.get_news`.
        3. Opens 'hist_news_output.txt' in write mode.
        4. Writes each article's key fields (excluding 'images' and 'content') to the file,
           with each article's data separated by newlines for readability.

    OUTPUT:
        - A file named 'hist_news_output.txt' containing key information for each news article,
          organized and separated for easy readability.

    RETURNS:
        None
"""
    hist_news_client = NewsClient(api_key=alpaca_api_key, secret_key=alpaca_secret_key)
    request_params = NewsRequest(
        symbols='AAPL',
        start=datetime(2024, 10, 21),
        exclude_contentless=True,
        limit=50
    )

    news_output = hist_news_client.get_news(request_params=request_params)
    with open('hist_news_output.txt', 'w') as f:
        news_list = news_output.data['news']

        for news in news_list:
            dict_news = dict(news)
            for symbol in dict_news.keys():
                if symbol != 'images' and symbol != 'content':
                    f.write(f"({symbol}, {dict_news[symbol]})\n")
            f.write("\n")


'''--------------------------------LIVE WEBSOCKET INFORMATION---------------------------------'''


async def live_websocket_data_handler(data):
    print(data)
    print()


# works
def stock_live_minute_bars():
    stream.subscribe_bars(live_websocket_data_handler, 'AAPL')
    stream.run()

# works
def stock_live_daily_bars():
    stream.subscribe_daily_bars(live_websocket_data_handler, 'AAPL')
    stream.run()

# works
def stock_live_quotes():
    stream.subscribe_quotes(live_websocket_data_handler, 'AAPL')
    stream.run()

# works
def stock_live_trades():
    stream.subscribe_trades(live_websocket_data_handler, 'AAPL')
    stream.run()

# inconclusive during testing
def stock_live_updated_bars():
    stream.subscribe_updated_bars(live_websocket_data_handler, 'AAPL')
    stream.run()

# inconclusive during testing (news is not a common output)
def stock_live_news():
    news_livestream = NewsDataStream(api_key=alpaca_api_key, secret_key=alpaca_secret_key)
    news_livestream.subscribe_news(live_websocket_data_handler, 'AAPL')
    news_livestream.run()


'''-------------------------------------EXECUTION SECTION-------------------------------------'''
# write function(s) to execute here
stock_live_news()

end_time = time.time()
print("Elapsed time:", end_time - start_time, "seconds")