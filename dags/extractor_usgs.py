import feedparser
import datetime

import requests, lxml
from bs4 import BeautifulSoup
from datetime import timedelta
from nlp_methods import to_no_punctuation

FEED_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.atom"
FEED = feedparser.parse(FEED_URL)

pointer = FEED.entries

def extract_info_from_entry(entry):

    title = to_no_punctuation(entry["title"].split(" "))
    time_str = entry["updated"]
    time = datetime.datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    url_link = entry["links"][0]["href"]
    location = entry["where"]

    title_county = title[-2]
    title_state = title[-1]
    title_magnitude = float(title[1])
    
    return {
        "title": title,
        "time_str": time_str,
        "time": time,
        "url_link": url_link,
        "location": location,
        "county": title_county,
        "state": title_state,
        "magnitude": title_magnitude
    }

if __name__ == "__main__":
    for feed in pointer:
        pass # store into database