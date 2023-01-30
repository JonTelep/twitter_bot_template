# ================================================================
# File Name: lib_openai.py
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
import openai
import json
from decouple import config

# Authentication of the openai module
# You must assign your openai organization id
openai.organization = config("OPENAI_ORG_ID")

# You must assign your openai API Key
openai.api_key = config("OPENAI_API_KEY")

def chatGPT_Request(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=280,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    textResponse = str(response)
    jsonResponse = json.loads(textResponse)
    chatGPT_Response = jsonResponse['choices'][0]['text']
    return chatGPT_Response

