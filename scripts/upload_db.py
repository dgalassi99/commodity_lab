import sqlite3
import pandas as pd

def upload_df_to_db(df: pd.DataFrame, db_path: str, table_name: str = 'prices'):
    """
    Upload a DataFrame to a specified table in SQLite DB.
    
    Args:
        df (pd.DataFrame): DataFrame with at least these columns:
            ['date', 'open', 'high', 'low', 'close', 'volume', 'name', 
             'ticker', 'category', 'source', 'timeframe']
        db_path (str): path to the SQLite database file
        table_name (str): table name to insert data into (default: 'prices')
    """
    conn = sqlite3.connect(db_path)
    
    # Upload with append mode, avoid adding index column
    df.to_sql(table_name, conn, if_exists='append', index=False)
    
    conn.close()
    print(f"Uploaded {len(df)} rows to {table_name} table in database at {db_path}")

