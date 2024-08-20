import logging, time
from langchain_community.chat_models import ChatOpenAI
from config_app.config import get_config
from langchain_groq import ChatGroq
from openai import OpenAI
import openai
import requests
# Cấu hình logging
import logging
import os
from groq import Groq

config_app = get_config()

# Danh sách các API key
api_keys = config_app['parameter']['grog_api_keys']
grog_api_keys_1= [
        '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',
        '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',
        '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',
        "sk-proj-w3azMwrCVPY4fIZFYKpXT3BlbkFJkzTwig65TQM4hqSaInwM"]

grog_api_keys_2 = [
        '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',
        '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',
        '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',
        "sk-proj-w3azMwrCVPY4fIZFYKpXT3BlbkFJkzTwig65TQM4hqSaInwM"]
grog_api_keys_3 = [
        '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',
        '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',
        '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',
        "sk-proj-w3azMwrCVPY4fIZFYKpXT3BlbkFJkzTwig65TQM4hqSaInwM"
    ]

current_key_index1 = 0
current_key_index2 = 0
current_key_index3 = 0

def get_llm1():
    global current_key_index1
    return get_llm(grog_api_keys_1, current_key_index1)

def get_llm2():
    global current_key_index2
    return get_llm(grog_api_keys_2, current_key_index2)

def get_llm3():
    global current_key_index3
    return get_llm(grog_api_keys_3, current_key_index3)

def get_llm(api_keys, current_key_index):
    # global current_key_index
    try:
        api_key = api_keys[current_key_index]
        if "gsk" in api_key:
            print('---- grog ----')
            print("key:", api_key)
            client = Groq(
            api_key=api_key,
            )

            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": "Hello World",
                    }
                ],
                model="llama3-8b-8192",
            )
            if response:
                return ChatGroq(model=config_app['parameter']['grog_model_to_use'], api_key=api_key)
        else:
            print('----openai----')
            print("key:", api_key)
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                        model="gpt-3.5-turbo-0125",
                        messages=[
                            {"role": "user","content": "Hello World"},
                        ]
                        )
            if response:
                return ChatOpenAI(model_name=config_app["parameter"]["gpt_model_to_use"], temperature=config_app["parameter"]["temperature"], openai_api_key=api_key)
    except Exception as e:
        logging.error(f"API returned an API Error: {e}")
        current_key_index = (current_key_index + 1) % len(api_keys)
        time.sleep(1)
        return get_llm()
    
def open_api_keys(api_keys):
    for api_key in api_keys:
        try:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                        model="gpt-3.5-turbo-0125",
                        messages=[
                            {"role": "user","content": "Hello World"},
                        ]
                        )
            if response:
                return api_key
        except openai.APIError as e:
            print(f"OpenAI API returned an API Error: {e}")
            
# print(get_llm())