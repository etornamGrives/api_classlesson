import tweepy
consumer_key = "xyQvle2YkuYWhz0MIgzDQ8SbY"
consumer_secret = "BAAGWU8WR0aF014O53555mFbW2nILxerusrqIiN12SqISFHBr1"
access_token = "1694714046401146880-IGEOSdZczTKKEY2Fbiw59xUigdCJJY"
access_token_secret = "yFy2fikNBS9R0LuqXypZeJw7bWpVO244iDuOoFjYDgt1Kpython "

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
