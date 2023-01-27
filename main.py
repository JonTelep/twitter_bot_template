import os
import sys

# Below adds the Twitter_Bots/Libraries/ directory as a sys path giving the ability to reference the libraries.
lib_tweepy = os.path.dirname(os.path.realpath("lib_tweepy.py"))
sys.path.append(lib_tweepy)

# importing lib_tweepy class for usage
from lib_tweepy import lib_tweepy

# Defaulting tweet content
tweet_content = "This is your first tweet!"

# Creating lib_tweepy object
tweepy_create_object = lib_tweepy(tweet_content, "DONOTREPLY","123")

# Executing Create Tweet function storing the tweet id from the response
tweet_id = lib_tweepy.Create_Tweet(tweepy_create_object)


reply_tweet_content = "This is your first reply to your own tweet!"
tweepy_reply_object = lib_tweepy(reply_tweet_content, tweet_id, "123")
reply_tweet_id = lib_tweepy.Reply_Tweet(tweepy_reply_object)
