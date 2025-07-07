import yfinance as yf
import pandas as pd

def fetch_spot_prices(
    tickers: dict, 
    period: str = "1mo", 
    interval: str = "1d", 
    source: str = "yfinance"
) -> pd.DataFrame:
    """
    Fetch historical spot price data for given tickers from Yahoo Finance.

    Args:
        tickers (dict): dict mapping name -> yfinance ticker string.
            Example for commodities:
            {
                "Gold": "GC=F",
                "Crude Oil": "CL=F",
                ...
            }
        period (str): data period to fetch, e.g. '1mo', '3mo', '1y'.
        interval (str): data frequency, e.g. '1d', '1wk', '1mo'.
        category (str): category of assets, e.g., 'commodity', 'forex', 'stock', 'etf'.
        source (str): data source identifier.

    Returns:
        pd.DataFrame: combined data with columns:
            ['date', 'open', 'high', 'low', 'close', 'volume',
             'name', 'ticker', 'category', 'source', 'timeframe']
    """
    all_data = []
    for name, ticker in tickers.items():
        print(f"Fetching  data for {name} ({ticker}) - Period: {period}, Interval: {interval}")
        data = yf.download(ticker, period=period, interval=interval)
        if data.empty:
            print(f"No data for {name} ({ticker})")
            continue
        
        df = data.reset_index()
        df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
        df.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
        
        # Add meta columns
        df['name'] = name
        df['ticker'] = ticker
        df['source'] = source
        df['timeframe'] = interval
        
        all_data.append(df)
    
    if all_data:
        return pd.concat(all_data, ignore_index=True)
    else:
        return pd.DataFrame(columns=['date', 'open', 'high', 'low', 'close', 'volume', 'name', 'ticker', 'category', 'source', 'timeframe'])
