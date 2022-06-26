import tweepy

auth = tweepy.OAuth1UserHandler(
    'x', 
    'xx',
    'xxx', 
    'xxxx'
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)