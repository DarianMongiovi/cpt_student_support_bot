# Imports for Tools
import json
import csv
from datetime import datetime
import os
import re

# This is the schema for the database, cannot be changed!!!
SCHEMA_COLUMNS = ["event_type", "event_name", "location", "date", "time", "source"]

def convert_json_to_csv():
    json_file_path = os.path.join("resources", "events", "processed_cmcc_info.json")

    # Load the JSON data
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Output CSV file
    output_csv = os.path.join("resources", "events", "calendar_events.csv")

    # Function to clean the event name (shrink "Commencement {random}" to "Commencement")
    def clean_event_name(event_name):
        event_name = re.sub(r"Commencement\s.*", "Commencement", event_name)
        return event_name

    # Function to check if the event name should be blacklisted (F-11 F-5 pattern)
    def is_blacklisted(event_name):
        return bool(re.search(r"\b[A-Za-z]-\d+\s[A-Za-z]-\d+\b", event_name))

    # Open the CSV file for writing
    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=SCHEMA_COLUMNS)
        writer.writeheader()  # Write the header row

        # Loop through each academic calendar
        for calendar in data["academic_calendars"]:
            start_year = calendar["start_year"]
            end_year = calendar["end_year"]
            year_code = f"{start_year}-{end_year[-2:]}"

            # Loop through each event in the academic calendar
            for event in calendar["events"]:
                # Skip events with "Revised" in the description
                if "Revised" in event["description"]:
                    continue

                # Skip events that match the (F-11 F-5 pattern) pattern
                if is_blacklisted(event["description"]):
                    continue

                # Clean up event name if it's "Commencement {random}"
                event_name = clean_event_name(event["description"])

                # Parse the event date and remove the time part
                event_date = datetime.strptime(event["date"], "%Y-%m-%d %H:%M:%S").date()

                # Create a row for each event
                row = {
                    "event_type": "academic_calendar",
                    "event_name": event_name,
                    "location": "CMCC",  # this is the location?
                    "date": event_date.strftime("%Y-%m-%d"),  # convert the date
                    "time": "00:00",  # the whole day?
                    "source": f"academic_calendar/{year_code}", # what calendar it is from
                }

                # Write the row to the CSV
                writer.writerow(row)

    print(f"CSV: Correctly formatted JSON and saved!")