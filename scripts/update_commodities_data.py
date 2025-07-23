import sys
import os

sys.path.append(os.path.dirname(__file__))

from scripts.fetch_yf_data import fetch_spot_prices
from upload_db import upload_df_to_db

def update_commodities(tickers, db_path="../../db/commodities.db", period='1y', interval='1d'):
    df = fetch_spot_prices(tickers, period=period, interval=interval)
    print(f'Fetched {len(df)} rows of data')

    upload_df_to_db(df, db_path)
    print('Data uploaded successfully')

