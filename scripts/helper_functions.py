import os
import pandas as pd
import sqlite3 as sql

def load_and_transform_csv(folder, base_name, date_str):
    """
    Load the CSV file based on folder, base_name, and date string,
    rename columns to standardized names,
    and parse the 'date' column to datetime.
    
    Args:
        folder (str): path to the folder containing the CSV file (with trailing slash)
        base_name (str): base filename prefix before the date
        date_str (str): date string in the filename (e.g., '07-23-2025')
    
    Returns:
        pd.DataFrame: transformed DataFrame ready for DB insertion
    """
    file_path = f"{folder}{base_name}{date_str}.csv"
    df = pd.read_csv(file_path)
    df = df.iloc[:-1]
    df = df.rename(columns={
        'Contract':'contract_id',
        'Last':'close',
        'Change':'change',
        'Open':'open',
        'High':'high',
        'Low':'low',
        'Previous':'previous',
        'Volume':'volume',
        'Open Interest':'open_interest',
        'Time':'date'
    })
    df['date'] = pd.to_datetime(df['date'])

    print(f"Loaded {len(df)} rows.")

    return df


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

def create_db_table(db_path, table_name, columns_of_db):
   '''db_path: path where the db is located
       table_name: name of the db table
       columns_of_db: columns to create
   '''
   print(f'Creating a table (if not existing) in {db_path}')
   conn = sql.connect(db_path)
   cursor = conn.cursor()

   cols_sql = ", ".join([f'"{col}" {dtype}' for col, dtype in columns_of_db.items()])
   sql_query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                    {cols_sql},
                    PRIMARY KEY (contract_id, date))"""
   cursor.execute(sql_query)
   conn.commit()
   conn.close()
    
def insert_df_in_db(df, db_path, table_name):
   '''df: dataframe to upload into the db
       db_path: path where the db is located
       table_name: name of the db table
   '''
   print(f"Inserting {len(df)} rows into '{table_name}' in database '{db_path}'.")
   conn = sql.connect(db_path)
   df.to_sql(table_name, conn, if_exists='append', index=False)
   conn.close()
   print("Data inserted successfully.")

   
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
