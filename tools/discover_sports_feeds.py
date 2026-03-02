import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://www.cmmustangs.com/"

def discover_schedule_pages():
    print("Fetching athletics homepage...")
    response = requests.get(BASE_URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    schedule_pages = set()

    for link in soup.select("a[href]"):
        href = link["href"]

        # Match URLs like /sports/bsb/2025-26/schedule
        if re.search(r"/sports/[^/]+/[^/]+/schedule$", href):
            full_url = urljoin(BASE_URL, href)
            schedule_pages.add(full_url)

    return sorted(schedule_pages)


def generate_ical_links(schedule_pages):
    print("\nGenerating ICS links...\n")
    ical_links = []

    for page in schedule_pages:
        ical_url = f"{page}?print=ical"
        ical_links.append(ical_url)

    return ical_links


if __name__ == "__main__":
    schedules = discover_schedule_pages()
    ical_urls = generate_ical_links(schedules)

    print("Discovered ICS Feeds:\n")
    for url in ical_urls:
        print(url)

    print(f"\nTotal feeds found: {len(ical_urls)}")