import os
import sys
from helper_functions import load_and_transform_csv, create_db_table, insert_df_in_db

if __name__ == "__main__":
    folder = "../data/raw/futures/WTI_crude_oil/"
    base_name = "crude-oil-wti-prices-end-of-day-"
    
    date_str = input("Enter the date (MM-DD-YYYY) of the file to load: ").strip()
    
    columns_of_db = {
        "contract_id": "TEXT",
        "close": "REAL",
        "change": "REAL",
        "open": "REAL",
        "high": "REAL",
        "low": "REAL",
        "previous": "REAL",
        "volume": "INTEGER",
        "open_interest": "INTEGER",
        "date": "TEXT"
    }
    
    db_path = "../db/WTI_futures.db"
    table_name = 'WTI_futures_data'
    
    try:
        data = load_and_transform_csv(folder, base_name, date_str)
        create_db_table(db_path, table_name, columns_of_db)
        insert_df_in_db(data, db_path, table_name)
    except Exception as e:
        print(f"Error: {e}")
