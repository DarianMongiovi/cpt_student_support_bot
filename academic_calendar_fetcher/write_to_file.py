# Imports for Tools
import json
import os

# --------------------------------------------------------
# Credit to Professor Bisesti for the original script.
# --------------------------------------------------------

def write_to_file(directory, academic_calendar):
    write_file = os.path.join(os.getcwd(), "resources", "events", "processed_cmcc_info.json")

    if not os.path.exists(write_file):
        info = {"academic_calendars": []}
    else:
        with open(write_file, "r") as f:
            info = json.load(f)

    calendars = info.get("academic_calendars", [])

    # Check for duplicates
    exists = any(
        cal["academic_year"] == academic_calendar["academic_year"]
        for cal in calendars
    )

    if not exists:
        calendars.append(academic_calendar)
        print(f"Added calendar {academic_calendar['academic_year']}")
    else:
        print(f"Duplicate calendar {academic_calendar['academic_year']} skipped")

    info["academic_calendars"] = calendars

    with open(write_file, "w") as f:
        json.dump(info, f, indent=4, default=str)