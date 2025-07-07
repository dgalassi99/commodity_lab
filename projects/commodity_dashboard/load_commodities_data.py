#reaching the useful scripts
import sys
sys.path.append('../../scripts')

from fetch_yf_spot_data import fetch_spot_prices
from upload_db import upload_df_to_db
import os

tickers = {
    "Gold": "GC=F",
    "Silver": "SI=F",
    "Crude Oil": "CL=F",
    "Natural Gas": "NG=F",
    "Copper": "HG=F",
    "Corn": "ZC=F",
    "Wheat": "ZW=F"
}

df = fetch_spot_prices(tickers,period = '1y',interval = '1d')
print(f'Fetched {len(df)} rows of data')

db_path = "../../db/commodities.db"
upload_df_to_db(df,db_path)

print('Data uploaded succesfully')