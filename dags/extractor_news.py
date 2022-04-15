import requests, lxml
import datetime

from datetime import timedelta

NEWS_API_KEY = "a66dff0b4c614ba1ac68eedfec007e85"
NEWS_URL = "https://newsapi.org/v2/everything"

def get_results(state="", county="", event_time=datetime.datetime.now(), *others):    
    query_params = {
        "q": [state, county, *others,"Earthquake"],
        "sortBy": "top",
        "language": "en",
        "from": datetime.datetime.strftime(event_time - timedelta(days=0), "%Y-%m-%dT%H:%M:%S%z"),
        "apiKey": NEWS_API_KEY
    }
    
    return requests.get(NEWS_URL, params=query_params)

if __name__ == "__main__":
    res = get_results(state="CA", county="Alameda",event_time=datetime.datetime.now() - timedelta(days=10))
    open_bbc_page = res.json()
    
    print(open_bbc_page)
    # extract information