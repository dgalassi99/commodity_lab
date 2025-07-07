import sqlite3 as sql
import os

#making sure db folder is there
os.makedirs("../db", exist_ok=True)
#path to db file
db_path = "../db/commodities.db"
#connect to the db
conn = sql.connect(db_path)
cursor = conn.cursor()

#creating the db table
cursor.execute("""
               CREATE TABLE IF NOT EXISTS prices(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               commodity TEXT NOT NULL,
               date DATE NOT NULL,
               open REAL,
               high REAL,
               low REAL,
               close REAL,
               volume REAL);""")

#commit and close db
conn.commit()
conn.close()

print(f'Database and table created at: {db_path}')