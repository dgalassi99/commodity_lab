import sqlite3 as sql
import os

def setup_db(db_name):
    # Ensure the db directory exists
    os.makedirs("../db", exist_ok=True)

    # Compose the full path to the db file
    db_path = f"../db/{db_name}.db"

    # Connect to SQLite database (creates the file if not exists)
    conn = sql.connect(db_path)
    cursor = conn.cursor()

    # Create the generic 'prices' table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT NOT NULL,
            date DATE NOT NULL,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume REAL,
            name TEXT,
            source TEXT,
            timeframe TEXT,
            UNIQUE(ticker, date, source, timeframe) ON CONFLICT IGNORE
        );
    """)

    conn.commit()
    conn.close()

    print(f"Database and table created at: {db_path}")


if __name__ == "__main__":
    db_name = input("Enter the name of the database to create (without extension): ").strip()
    if db_name:
        setup_db(db_name)
    else:
        print("No database name provided. Exiting.")
