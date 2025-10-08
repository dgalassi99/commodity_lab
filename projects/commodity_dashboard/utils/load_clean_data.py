import os
import sqlite3
import pandas as pd
from .data_cleaning import interpolate_missing_business_days

# ------------------------------
# Automatically locate the database relative to project root
# ------------------------------
# __file__ points to this script
# Go up three levels: utils/ -> commodity_dashboard/ -> projects/ -> commodity_lab/
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DB_PATH_DEFAULT = os.path.join(PROJECT_ROOT, "db", "WTI_futures.db")

# ------------------------------
# Load raw data from DB
# ------------------------------
def load_raw_data(db_path=DB_PATH_DEFAULT, table_name="WTI_futures_data"):
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database not found at {db_path}")
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    df['date'] = pd.to_datetime(df['date'])
    conn.close()
    return df

# ------------------------------
# Load and clean data
# ------------------------------
def load_and_clean_data(db_path=DB_PATH_DEFAULT):
    df = load_raw_data(db_path)
    clean_df = interpolate_missing_business_days(df)
    return clean_df
