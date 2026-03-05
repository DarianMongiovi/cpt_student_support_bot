import os
import sys
import json

if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

    base_path = os.path.dirname(base_path) 

def write_to_file(directory, academic_calendar):
    target_dir = os.path.join(base_path, "resources", "events")
    os.makedirs(target_dir, exist_ok=True)
    
    write_file = os.path.join(target_dir, "processed_cmcc_info.json")

    if not os.path.exists(write_file):
        info = {"academic_calendars": []}
    else:
        with open(write_file, "r") as f:
            info = json.load(f)

    calendars = info.get("academic_calendars", [])

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
