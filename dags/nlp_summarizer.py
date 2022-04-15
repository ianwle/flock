from nlp_methods import *

# How to use sentiment analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sid_object = SentimentIntensityAnalyzer()
sid_object.polarity_scores(text)

# for i in bs(requests.get(extract_news_all(daydelta=-3)["articles"][0]["url"]).text).find_all('p'):
#     ...:     my_text.append(i.text)
