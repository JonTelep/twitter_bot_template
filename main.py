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
from Openai.lib_openai import chatGPT_Request

# Storing chatGPT's response of the defaulted prompt
chatgpt_response = chatGPT_Request("Tell me a joke about the Ethereum blockchain.")
print(chatgpt_response)

# Creating lib_tweepy object
tweepy_create_object = lib_tweepy(chatgpt_response, "DONOTREPLY","123")

# Executing Create Tweet function storing the tweet id from the response
tweet_id = lib_tweepy.Create_Tweet(tweepy_create_object)

print("Your first Tweet ID is: " + tweet_id)