Academic/Sports Calendar Database Populator

This program is designed to scrape and clean data from multiple sources, then create and populate the events table in the PostgreSQL database.

Language Version: Python 3.14.3
Database: PostgreSQL
Key Libraries: pandas, sqlalchemy, dotenv, icalendar

Database Schema:
Table: events
id SERIAL Primary Key
event_type TEXT
event_name TEXT
location TEXT
date TEXT
time TEXT
source TEXT

*Replace dummy values in env file accordingly, and run postgre_populate.py to initiate program.

Directory Table:
/
├── academic_calendar_fetcher/
│   ├── __pycache__/
│   ├── resources/
│   ├──   ├── calendars/
│   ├──   ├── events/
│   ├── __init__.py
│   ├── convert_json_to_csv.py
│   ├── fetch_calendar.py
│   ├── main.py
│   ├── process_file.py
│   ├── write_to_file.py
├── config/
│   ├── __pycache__/
│   ├── sports_feeds.py
├── db/
│   ├── aggregation.db
├── resources/
│   ├── calendars/
│   ├── events/
├── tools/
│   ├── discover_sports_feeds.py
├── events.env
├── postgre_populate.py
├── sports_etl.py
