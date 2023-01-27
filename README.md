# twitter_bot_template
This Repository will house all code and frameworks around creating a simple Twitter Bot

This template can be used to get a quick twitter bot up and running. Utilizes ```lib_tweepy_auth.py``` to authenticate a user to the Twitter API. ```lib_tweepy.py``` houses the lib_tweepy class which calls the authentication and references many requests to the Twitter API.

## Installations
Below will show all necessary installations needed to run
#### tweepy (Required)
```$pip install tweepy```
Used to reference the python library for easy Twitter API Auth and function calling. Tweepy utilizes python's Request library to make the calls.

### python-decouple (Required)
```$pip install python-decouple```
Used to reference API keys from the .env file. ```.env``` can be altered to get your own .env file up and running!
`NOTE` you must change the file ```template.env.txt``` to ```.env``` as well as add your own keys to the .env for this to work.

## Sample Usage
Please reference ```main.py``` to see a sample execution

## Sample Output
Below is an image that shows what would be tweeted in this guide:
![First Tweet](First_Tweet.png)
