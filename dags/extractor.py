import requests, lxml, datetime
from bs4 import BeautifulSoup as bs
from datetime import timedelta
import pandas as pd
import feedparser

from nlp_methods import to_no_punctuation
from newsapi import NewsApiClient

"""
http://rss.cnn.com/rss/cnn_topstories.rss
https://www.nytimes.com/services/xml/rss/nyt/HomePage.xml
http://www.npr.org/rss/rss.php?id=1001
https://www.yahoo.com/news/rss
https://www.latimes.com/local/rss2.0.xml
http://feeds.abcnews.com/abcnews/topstories
https://www.nbcnews.com/id/3032091/device/rss/rss.xml
https://sanfrancisco.cbslocal.com/feed/
https://www.chicagotribune.com/rss2.0.xml
https://www.theguardian.com/world/natural--disasters/rss
https://www.theguardian.com/world/earthquakes/rss
http://feeds.bbci.co.uk/news/rss.xml
http://feeds.bbci.co.uk/news/science_and_environment/rss.xml
"""

NEWS_SOURCES = [
    "cbs-news", "reuters", "cnn", "usa-today", "bbc-news"
    "The Guardian", "New York Times", "Ca.gov"
]

FEED_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.atom"

NEWS_API_KEY = "a66dff0b4c614ba1ac68eedfec007e85"
NEWS_URL = "https://newsapi.org/v2/everything"


# newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def extract_usgs_feed_all():
    return feedparser.parse(FEED_URL)

def extract_usgs_details(entry):
    try:
        title = to_no_punctuation(entry["title"].split(" "))
        print(entry)
        time_str = entry["updated"]
        time = datetime.datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        url_link = entry["links"][0]["href"]
        location = entry["where"]
        depth = bs(entry["summary"]).find_all("dd")[-1].text.split(" (")
        # print(entry["title"], title, title[0:3])
        depth_km = depth[0].split(" ")[0]
        depth_mi = depth[1].split(" ")[0]

        title_county = title[-2]
        title_state = title[-1]
        title_magnitude = float("{}.{}".format(title[1], title[2]))
        
        return {
            "title": " ".join(title),
            "time_str": time_str,
            "time": time,
            "url_link": url_link,
            "location": location,
            "county": title_county,
            "state": title_state,
            "magnitude": title_magnitude,
            "depth_km": depth_km,
            "depth_mi": depth_mi
        }
    
    # Skip it
    except AttributeError as e: pass
    except Exception as e: pass

def extract_news_all(event_time=datetime.datetime.now(), daydelta=0, *others):    
    all_articles = newsapi.get_everything(q='ukraine',
                                          sources=','.join(NEWS_SOURCES),
                                        #   domains='bbc.co.uk,techcrunch.com',
                                          from_param=datetime.datetime.strftime(event_time,"%Y-%m-%dT%H:%M:%S%z"),
                                          to=datetime.datetime.strftime(event_time + timedelta(days=daydelta), "%Y-%m-%dT%H:%M:%S%z"),
                                          language='en',
                                          sort_by='relevancy')
                                        #   page=2)

    return all_articles

def extract_bbc_paragraphs():
    pass

# How to use sentiment analysis
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# sid_object = SentimentIntensityAnalyzer()
# sid_object.polarity_scores(text)


# for i in bs(requests.get(extract_news_all(daydelta=-3)["articles"][0]["url"]).text).find_all('p'):
#     ...:     my_text.append(i.text)
