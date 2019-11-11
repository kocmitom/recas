import tweepy
from recas import credentials
import time

def get_auth():
    cr = credentials.twitter_credentials()
    auth = tweepy.OAuthHandler(cr['CONSUMER_KEY'], cr['CONSUMER_SECRET'])
    auth.set_access_token(cr['OAUTH_TOKEN'], cr['OAUTH_TOKEN_SECRET'])
    api = tweepy.API(auth)
    return api

def get_tweet_list(twapi, idlist):
    '''
    Invokes bulk lookup method.
    Raises an exception if rate limit is exceeded.
    '''
    # fetch as little metadata as possible
    tweets = twapi.statuses_lookup(id_=idlist, include_entities=False, trim_user=True)
    if len(tweets) ==0:
        print('get_tweet_list: unexpected response size %d, expected %d', len(tweets), len(idlist))
        Logger.warn("incorrect")
    all_tweets = {}
    for tweet in tweets:
        all_tweets[tweet.id] = tweet.text 

    # quessed API limit waiting
    print("sleeping 3 sec") 
    time.sleep(3)
    return all_tweets

def get_tweets_bulk(idlist):
    twapi = get_auth()
    batch_size=100 # API restriction
    # process IDs from the file
    all_tweets = {}
    tweet_ids = []
    for tweet_id in idlist:
        tweet_ids.append(tweet_id)
        # API limits batch size
        if len(tweet_ids) == batch_size:
            all_tweets.update(get_tweet_list(twapi, tweet_ids))
            tweet_ids = []
    # process remainder
    if len(tweet_ids) > 0:
        all_tweets.update(get_tweet_list(twapi, tweet_ids))

    return all_tweets
