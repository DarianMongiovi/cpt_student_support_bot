from __future__ import annotations
import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

###############################################################################
#                               DATABASE SETUP                                #
###############################################################################

load_dotenv("events.env")

# Build the Connection String
DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine = create_engine(DB_URL)

def initialize_db():
    with engine.begin() as conn:
        conn.execute(text('''
            CREATE TABLE IF NOT EXISTS events (
                id SERIAL PRIMARY KEY,
                event_type TEXT,
                event_name TEXT,
                location TEXT,
                date TEXT,
                time TEXT,
                source TEXT
            )
        '''))
    print("PostgreSQL Database initialized.")

###############################################################################
#                               DATABASE POPULATE                             #
###############################################################################

def db_populate(df):
    schema_cols = ['event_type', 'event_name', 'location', 'date', 'time', 'source']

    valid_df = df[schema_cols]

    valid_df.to_sql('events', engine, if_exists='append', index=False)
    print("db successfully populated")

if __name__ == "__main__":
    initialize_db()

    #Populate Sports Data
    from sports_etl import final_sports_df
    sports_df = final_sports_df()
    db_populate(sports_df)