import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


#enter twitter API tokens here
access_key = ""
access_secret = ""
consumer_key = ""
consumer_secret = ""


# Twitter authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)


# creating an API object
api = tweepy.API(auth)


tweets = api.user_timeline(screen_name = '@TwitterUsername',
                            # 200 is maximum count allowed
                            count = 200,
                            include_rts = False,
                            tweet_mode =  'extended'
                            ) 


tweet_list = []
for tweet in tweets:
    text =  tweet._json["full_text"]

    refined_tweet = {"user" : tweet.user.screen_name,
                    'text' : text,
                    'favorite_count' : tweet.favorite_count,
                    'retweet_count' : tweet.retweet_count,
                    'created_at' : tweet.created_at  }

    tweet_list.append(refined_tweet)                

#create a csv file for pulled tweets
df = pd.DataFrame(tweet_list)
df.to_csv("file_name.csv")