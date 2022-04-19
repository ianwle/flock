import tweepy, json, requests
from nlp_methods import to_clean_tokens

BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAAP4hYwEAAAAArxtwzeiOgyvK9uAveTAZTgXas9A%3DWZEpItVlzdwTxC6CvfgIwsNmeW8xVA7sOJ9pyUPtVHbODwc8Ql"
ACCESS_TOKEN="1488797460470272000-5H19MGvoWlSmMkmbs3ykxCa4tDu779"
ACCESS_TOKEN_SECRET="z1aECz7pMRR2Wv6U8gv0IyUHxv0Dmg77vuHdfObxIvmgV"
CONSUMER_KEY="18k1Ep9RDUGyvbnrVseExDXQa"
CONSUMER_SECRET="JArpYJcFAJDe1Oos7Tus1kNRQFrzVsHSD2hvJBopV0dmtkFfVj"

auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

client = tweepy.Client(bearer_token=BEARER_TOKEN,
                      consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token=ACCESS_TOKEN,
                      access_token_secret=ACCESS_TOKEN_SECRET,
                      return_type=requests.Response,
                      wait_on_rate_limit=True)

tweets = api.search_tweets(q="Hello world", count=200, geocode="37.781157,-122.398720,10km", tweet_mode="extended")

def merge_tweets(bounding_box):
    for (lat, lng) in bounding_box:
        tweets = api.search_tweets(
            q="Hello world", count=200, geocode="37.781157,-122.398720,10km", tweet_mode="extended")

def get_tweets(query, geocode, count=200,):
    return api.search_tweets(q=query, count=count, geocode=geocode, tweet_mode="extended")

def get_twitter_feeds_30_days_prior():
    pass

def get_twitter_feeds_30_days_after():
    pass

def get_twitter_feeds_on_day():
    pass