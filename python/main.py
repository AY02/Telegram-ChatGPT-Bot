from dotenv import load_dotenv
import os
import telebot
from chatgpt import *
from functions import *

load_dotenv()

TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')

bot = telebot.TeleBot(TELEGRAM_API_KEY)


@bot.message_handler(commands=['ask_gpt'])
def ask_gpt(message):
    request = message.text.split(' ', 1)[1]
    log(f'{message.from_user.username}: {request}')
    #response = ask_chatgpt(request)
    response = 'You are too poor to afford ChatGPT'
    bot.reply_to(message, response)
    log(f'Chat GPT: {response}')



bot.polling()
