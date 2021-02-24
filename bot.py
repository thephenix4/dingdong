import telegram
import sys
import os
TOKEN = ['1666045843:AAEIzQl3CIEUVf0c71Hh2pJZYlgez5hxjMM']
CHAT_ID = XXXXXXXX
def send_message(event, context):
    bot = telegram.Bot(token=TOKEN)
    bot.sendMessage(chat_id = CHAT_ID, text = ‘Hey there!’)