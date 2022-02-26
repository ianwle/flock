import requests, lxml, datetime
from bs4 import BeautifulSoup as bs
from datetime import timedelta
import pandas as pd
from nlp_methods import to_no_punctuation

import feedparser

FEED_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.atom"

NEWS_API_KEY = "a66dff0b4c614ba1ac68eedfec007e85"
NEWS_URL = "https://newsapi.org/v2/everything"

def extract_usgs_feed_all():
    return feedparser.parse(FEED_URL)

def extract_usgs_details(entry):
    title = to_no_punctuation(entry["title"].split(" "))
    time_str = entry["updated"]
    time = datetime.datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    url_link = entry["links"][0]["href"]
    location = entry["where"]

    title_county = title[-2]
    title_state = title[-1]
    title_magnitude = float("{}.{}".format(title[1], title[2]))
    
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

def extract_news(state="", county="", event_time=datetime.datetime.now(), *others):    
    query_params = {
        "q": [state, county, *others,"Earthquake"],
        "sortBy": "top",
        "language": "en",
        "from": datetime.datetime.strftime(event_time - timedelta(days=0),
                                           "%Y-%m-%dT%H:%M:%S%z"),
        "apiKey": NEWS_API_KEY
    }
    
    return requests.get(NEWS_URL, params=query_params)
