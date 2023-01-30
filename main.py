# ================================================================
# File Name: main.py
# Created by: Telep IO https://www.telep.io/
# Date: 1/28/2023
# 
# Prerequisites
# 1. Install necessary libraries found in the README.md 
# 2. Apply for twitter API access: https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api
# 3. Generate necessary tokens found in Alter template.env.txt
# 4. Enter your newly generated tokens into the .env file
# 5. Send your first tweet!
# ================================================================
import os
import sys

# Below adds the Twitter_Bots/Libraries/ directory as a sys path giving the ability to reference the libraries.
lib_tweepy = os.path.dirname(os.path.realpath("lib_tweepy.py")) + '/Twitter'
sys.path.append(lib_tweepy)

# importing lib_tweepy class for usage
from lib_tweepy import lib_tweepy

# Defaulting tweet content
tweet_content = "This is your first tweet!"

# Creating lib_tweepy object
tweepy_create_object = lib_tweepy(tweet_content, "DONOTREPLY","123")

# Executing Create Tweet function storing the tweet id from the response
tweet_id = lib_tweepy.Create_Tweet(tweepy_create_object)

reply_tweet_content = "If you're seeing this, you're going to make it."
tweepy_reply_object = lib_tweepy(reply_tweet_content, tweet_id, "123")
reply_tweet_id = lib_tweepy.Reply_Tweet(tweepy_reply_object)