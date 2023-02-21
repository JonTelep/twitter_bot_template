# ================================================================
# File Name: main.py
# Created by: Telep IO https://www.telep.io/
# Date: 1/28/2023
# 
# Prerequisites
# 1. Install necessary libraries found in the README.md 
# 2. Apply for openai API access: https://beta.openai.com/account/api-keys
# 3. Generate necessary tokens found in Alter template.env.txt
# 4. Enter your newly generated tokens into the .env file
# 5. Send your first openai request!
# ================================================================
import os
import sys

# Below adds the ~/Twitter/ directory as a sys path giving the ability to reference the libraries.
lib_tweepy = os.path.dirname(os.path.realpath("lib_tweepy.py")) + '/Twitter'
sys.path.append(lib_tweepy)

# Below adds the ~/Openai/ directory as a sys path giving the ability to reference the libraries.
lib_openai = os.path.dirname(os.path.realpath("lib_openai.py")) + '/Openai'
sys.path.append(lib_openai)

from lib_tweepy import lib_tweepy
from lib_openai import chatGPT_Request
from randomize_prompts import give_me_a_prompt

# This helper function will divide text into sections of 280 characters to abide by Twitter's 280 character tweet limit
def divide_text(text):
    chunks = []
    while len(text) > 280:
        chunk = text[:280].rsplit(' ', 1)[0]
        chunks.append(chunk)
        text = text[len(chunk):].lstrip()
    if text:
        chunks.append(text)
    return chunks

# Storing chatGPT's response of the defaulted prompt
chatgpt_response = chatGPT_Request(give_me_a_prompt())
divided_response = divide_text(chatgpt_response)

# Index tracker to keep track of tweet ids and accurately tweet a reply if chatGPT response is longer than 280 characters
i = 0
for r in divided_response:
    if i > 0 :
        if i > 1 :
            tweepy_reply_object = lib_tweepy(r, reply_tweet_id)
        else:
            tweepy_reply_object = lib_tweepy(r, tweet_id)
        reply_tweet_id = lib_tweepy.Reply_Tweet(tweepy_reply_object)
        print("Reply Tweeted" + reply_tweet_id)
        print(r)
    else:
        # Creating lib_tweepy object
        tweepy_create_object = lib_tweepy(r)
        # Executing Create Tweet function storing the tweet id from the response
        tweet_id = lib_tweepy.Create_Tweet(tweepy_create_object)
        print("Tweeted" + tweet_id)
        print(r)
    i += 1