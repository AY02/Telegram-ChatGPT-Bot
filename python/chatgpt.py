import openai
from dotenv import load_dotenv
import os

load_dotenv()

CHATGPT_API_KEY = os.getenv('CHATGPT_API_KEY')

openai.api_key = CHATGPT_API_KEY

messages = [{'role': 'system', 'content': 'You are a intelligent assistant.'}]

def ask_chatgpt(request):
    if request is None:
        return
    messages.append({'role': 'user', 'content': request})
    completion = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = messages
    )
    response = completion['choices'][0]['message']['content']
    messages.append({'role': 'assistant', 'content': response})
    return response
