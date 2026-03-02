# Imports for Tools
import requests
import re
import os

# Website link and save folder path:
PAGE_URL = "https://www.cmcc.edu/academics/academic-calendar/"
SAVE_DIR = "resources/calendars"
BASE_UPLOAD = "https://www.cmcc.edu"  # for broken links

# This is so that we hopefully do not get blocked from the website:
headers = {"User-Agent": "Mozilla/5.0"}

# Make sure save folder exists
os.makedirs(SAVE_DIR, exist_ok=True)

def fetch_calendars():
    # Download HTML
    response = requests.get(PAGE_URL, headers=headers)
    response.raise_for_status()
    html = response.text

    # Scrape for any PDFs that match this format
    # I had some issues just changing the year dates on the download link, because the 
    # link also contains the upload year and month...
    matches = re.findall(r'href=["\'](.*?Academic-Calendar-\d{4}-\d{4}\.pdf)["\']', html)

    # Copy all found PDF links to our calendars folder for later!
    for link in set(matches):
        if link.startswith("http"):
            full_url = link
        else:
            full_url = BASE_UPLOAD + link  # if the path is relative add the front part!

        filename = full_url.split("/")[-1]
        filepath = os.path.join(SAVE_DIR, filename)

        pdf = requests.get(full_url, headers=headers)
        pdf.raise_for_status()

        with open(filepath, "wb") as f:
            f.write(pdf.content)

        print(f"Downloaded: {filepath}") # success!