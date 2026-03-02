# Imports for Tools
from datetime import datetime, timedelta
import os
import PyPDF2
import re

# Imports for Local
from . import write_to_file

# --------------------------------------------------------
# Credit to Professor Bisesti for the original script.
# --------------------------------------------------------

def read_calendar_file(directory, file):
    text = ""
    file_path = os.path.join(directory, file)

    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

    return text


def collectDate(line, event_year):
    comma_index = line.find(",")

    firstNumber = re.search(r"\d", line[comma_index:])
    if not firstNumber:
        return None, None, None, None

    firstCapitalAfterNumber = re.search(
        r"[A-Z]", line[comma_index + firstNumber.start() :]
    )

    if not firstCapitalAfterNumber:
        return None, None, None, None

    date_string = (
        line[
            comma_index + 1 : comma_index
            + firstNumber.start()
            + firstCapitalAfterNumber.start()
        ]
        + " "
        + event_year
    )

    date_string = date_string.replace(" ", "")
    return date_string, comma_index, firstNumber, firstCapitalAfterNumber


def checkYear(date, academic_calendar):
    if date.month <= 7:
        return datetime(
            year=int(academic_calendar["end_year"]),
            month=date.month,
            day=date.day,
        )
    return date


def clean_line(line, most_recent_date, academic_calendar):
    first_character = (len(line) - len(line.lstrip(" ")))
    events = []

    if first_character == 0 and "," in line:
        result = collectDate(line, academic_calendar["start_year"])
        if result[0] is None:
            return [], most_recent_date

        date_string, comma_index, firstNumber, firstCapitalAfterNumber = result

        # Date range
        if "-" in date_string:
            date_parts = date_string.split("-")
            start_date_string = date_parts[0]
            end_date_string = date_parts[1]

            start_date_part = datetime.strptime(start_date_string, "%B%d")
            end_date_part = datetime.strptime(end_date_string, "%d%Y")

            start_date = datetime(
                year=end_date_part.year,
                month=start_date_part.month,
                day=start_date_part.day,
            )

            end_date = datetime(
                year=end_date_part.year,
                month=start_date_part.month,
                day=end_date_part.day,
            )

            start_date = checkYear(start_date, academic_calendar)
            end_date = checkYear(end_date, academic_calendar)

            for single_date in (
                start_date + timedelta(n)
                for n in range((end_date - start_date).days + 1)
            ):
                event = {
                    "date": single_date,
                    "description": line[
                        comma_index
                        + firstNumber.start()
                        + firstCapitalAfterNumber.start() :
                    ].strip(),
                }
                most_recent_date = single_date
                events.append(event)

        else:
            try:
                event_date = datetime.strptime(date_string, "%B%d%Y")
            except ValueError:
                return [], most_recent_date

            event_date = checkYear(event_date, academic_calendar)
            most_recent_date = event_date

            event = {
                "date": event_date,
                "description": line[
                    comma_index
                    + firstNumber.start()
                    + firstCapitalAfterNumber.start() :
                ].strip(),
            }

            events.append(event)

    else:
        if most_recent_date is None:
            return [], most_recent_date

        events.append(
            {"date": most_recent_date, "description": line.strip()}
        )

    return events, most_recent_date


def get_academic_year(fall_text):
    fallLines = fall_text.split("\n")
    if not fallLines:
        return ""

    calendarYearComponents = fallLines[0].strip().split()
    return " ".join(calendarYearComponents)


# Main Function that read the calenders
def process_file(directory, file):
    print("Processing File:", file)

    text = read_calendar_file(directory, file)

    # Extract years safely using regex
    years = re.findall(r"\d{4}", file)
    if len(years) < 2:
        raise ValueError(f"Could not extract years from filename: {file}")

    academic_calendar = {
        "academic_year": get_academic_year(text),
        "start_year": years[0],
        "end_year": years[1],
        "events": [],
    }

    print("Building Academic Calendar for", academic_calendar["academic_year"])

    pdfLines = text.split("\n")

    allEvents = []
    most_recent_date = None

    for i, line in enumerate(pdfLines[3:], start=3):

        if "class meeting" in line.lower():
            continue

        if not line.strip():
            continue

        if ":" in line and len(line) < 50:
            continue

        if "approved" in line.lower():
            continue

        if len(line) in range(10, 19) and any(char.isdigit() for char in line):
            continue

        # Continuation of previous event
        if most_recent_date and (
            line.lstrip()[0].islower() or line.lstrip()[0].isdigit()
        ):
            if allEvents:
                allEvents[-1]["description"] += " " + line.strip()
            continue

        events, most_recent_date = clean_line(
            line, most_recent_date, academic_calendar
        )
        allEvents.extend(events)

    academic_calendar["events"] = allEvents
    write_to_file.write_to_file(directory, academic_calendar)

    return academic_calendar