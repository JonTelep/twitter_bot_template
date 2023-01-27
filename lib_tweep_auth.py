# ================================================================
# File Name: lib_tweepy_auth.py
# Created by: Telep IO
# Date: 2/7/2022
# 
# Prerequisites
# 1. Install necessary libraries found in the README.md 
# 2. Apply for Twitter API access: https://developer.twitter.com/en/portal/dashboard
# 3. Generate necessary tokens found in Alter template.env.txt
# 4. Enter your newly generated tokens into the .env file
# 5. Send your first tweet!
# ================================================================

import tweepy
from decouple import config

# Twitter keys for the individual developer project
consumer_key = config("TWITTER_API_KEY")
consumer_secret = config("TWITTER_API_KEY_SECRET")

# Twitter keys for the individual account
access_token = config("TWITTER_ACCESS_TOKEN")
access_token_secret = config("TWITTER_TOKEN_SECRET")

def OAuth():
    try:
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret,
                                access_token, access_token_secret)
        api = tweepy.API(auth)
        return api
    except ValueError:
        return print("Failed to authenticate")
