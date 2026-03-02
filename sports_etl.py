from __future__ import annotations

import re
import time
from datetime import datetime
from typing import Optional

import pandas as pd
import requests
from icalendar import Calendar

SCHEMA_COLUMNS = ["event_type", "event_name", "location", "date", "time", "source"]


def _clean_event_name(name: Optional[str]) -> Optional[str]:
    if not name:
        return None
    s = str(name).strip()
    # Remove leading "(Sport) " prefix commonly found in these feeds
    s = re.sub(r"^\([^)]+\)\s*", "", s)
    return s or None


def _dt_to_date_time_strings(dt) -> tuple[Optional[str], Optional[str]]:
    """
    dt can be a date or datetime
    Returns (YYYY-MM-DD, HH:MM) or (YYYY-MM-DD, None)
    """
    if dt is None:
        return None, None

    # date only events
    if not isinstance(dt, datetime):
        try:
            return dt.isoformat(), None
        except Exception:
            return None, None

    # datetime events 
    return dt.date().isoformat(), dt.strftime("%H:%M")


def _source_label_from_url(url: str) -> str:
    """
    Create a simple, unique, consistent source label from a CMCC athletics URL
    Example:
      https://www.cmmustangs.com/sports/bsb/2025-26/schedule?print=ical
      -> bsb/2025-26
      https://www.cmmustangs.com/sports/mbkb/2025-26jv/schedule?print=ical
      -> mbkb/2025-26jv
    """
    try:
        return url.split("/sports/")[1].split("/schedule")[0]
    except Exception:
        return "unknown_source"


def load_ics_events(
    url: str,
    *,
    source_label: str,
    event_type: str = "sports",
    timeout: int = 25,
    max_retries: int = 3,
    retry_delay_sec: float = 1.0,
) -> pd.DataFrame:
    """
    Returns an empty DataFrame on failure (and prints a WARNING)
    """
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/calendar, text/plain, */*",
    }

    last_err: Optional[Exception] = None

    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.get(url, headers=headers, timeout=timeout)
            resp.raise_for_status()

            # Guard: empty content -> treat as failure, retry
            if not resp.content or resp.content.strip() == b"":
                raise ValueError("Empty ICS content (b'') returned")

            cal = Calendar.from_ical(resp.content)
            break  # success
        except Exception as e:
            last_err = e
            if attempt < max_retries:
                time.sleep(retry_delay_sec)
            else:
                print(f"WARNING: Failed to load/parse ICS after {max_retries} attempts: {url} ({e})")
                return pd.DataFrame(columns=SCHEMA_COLUMNS)

    # If we get here, cal exists
    rows = []
    for component in cal.walk():
        if component.name != "VEVENT":
            continue

        summary = component.get("SUMMARY")
        location = component.get("LOCATION")
        dtstart = component.get("DTSTART")

        start_dt = dtstart.dt if dtstart else None
        date_str, time_str = _dt_to_date_time_strings(start_dt)

        rows.append(
            {
                "event_type": event_type,
                "event_name": _clean_event_name(summary),
                "location": str(location).strip() if location else None,
                "date": date_str,
                "time": time_str,
                "source": source_label,
            }
        )

    return pd.DataFrame(rows, columns=SCHEMA_COLUMNS)


def build_sports_dataframe(
    feeds: list[dict],
    season_filter: str | None = None,
    per_request_delay_sec: float = 0.5,
) -> pd.DataFrame:
    """
    Loop over all sports ICS feeds and return one unified DataFrame
    - season_filter: substring match against URL (e.g. "2025-26")
      Note: "2025-26" will also match "2025-26jv" (expected)
    - per_request_delay_sec: small delay to reduce rate limiting
    """
    dfs: list[pd.DataFrame] = []

    for feed in feeds:
        url = feed["url"]

        if season_filter and season_filter not in url:
            continue

        source_label = _source_label_from_url(url)

        df = load_ics_events(
            url,
            source_label=source_label,
            event_type="sports",
        )

        if not df.empty:
            dfs.append(df)

        # reduce chance of rate limiting / blank responses
        if per_request_delay_sec and per_request_delay_sec > 0:
            time.sleep(per_request_delay_sec)

    if not dfs:
        return pd.DataFrame(columns=SCHEMA_COLUMNS)

    sports_df = pd.concat(dfs, ignore_index=True)

    # Basic cleanup
    sports_df["event_name"] = sports_df["event_name"].astype(str).str.strip()
    sports_df.loc[sports_df["event_name"].isin(["None", "nan", ""]), "event_name"] = None
    sports_df = sports_df.dropna(subset=["event_name", "date"])

    # Dedupe
    sports_df = sports_df.drop_duplicates(subset=["source", "date", "time", "event_name"])

    return sports_df[SCHEMA_COLUMNS]


def final_sports_df():
    from config.sports_feeds import SPORT_ICS_FEEDS

    # Set to "2025-26" to only pull the 25-26 season (includes 25-26jv).
    # Set to None to pull all seasons in the config list.
    season = "2025-26"

    df = build_sports_dataframe(SPORT_ICS_FEEDS, season_filter=season)
    return df