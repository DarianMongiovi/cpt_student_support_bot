# Imports for Tools
import os
import pandas as pd

# Imports for Local
from academic_calendar_fetcher import process_file
from academic_calendar_fetcher import fetch_calendar
from academic_calendar_fetcher import convert_json_to_csv

def final_academic_df():
    # Is where the calenders will be kept and files will be worked on.
    directory = os.path.join(os.getcwd(), "resources", "calendars")

    # Fetches the calenders from the CMCC website for the current and past calendar.
    fetch_calendar.fetch_calendars()

    # Runs on each of the calendars in the calendars directory.
    for file in os.listdir(directory):
        if file.endswith(".pdf"):
            process_file.process_file(directory, file)
        
    # Converts the json to csv.
    convert_json_to_csv.convert_json_to_csv()

    file_path = os.path.join(os.getcwd(), "resources", "events", "calendar_events.csv")
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])

    return df
