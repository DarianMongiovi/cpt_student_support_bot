from __future__ import annotations
import os
import sys
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

###############################################################################
#                               DATABASE SETUP                                #
###############################################################################

if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

env_path = os.path.join(base_path, "events.env")
load_dotenv(env_path)

DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME')}"

try:
    engine = create_engine(DB_URL)
    with engine.connect() as conn:
        print("Successfully connected to the database!")
    
    # Your population logic here
    

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

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

        conn.execute(text('TRUNCATE TABLE events RESTART IDENTITY'))
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

    #Populate Academic Calendar Data
    from academic_calendar_fetcher.main import final_academic_df
    academic_df = final_academic_df()
    db_populate(academic_df)
