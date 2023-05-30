import random
import requests
import telebot
from telebot import types
from bs4 import BeautifulSoup
bot=telebot.TeleBot("6224837918:AAFwLF2VnEwxM46vmp28a2uoSQKIWgYpYYQ")
@bot.message_handler(commands=['start'])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("USD")
    item2 = types.KeyboardButton("EUR")
    item3 = types.KeyboardButton("PLN")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(m.chat.id, "Оберіть валюту", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handler_text(message):
    if message.text.strip()=='USD':
        response = requests.get('https://minfin.com.ua/ua/currency/usd/')
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            dollar = soup.find('div', {"class": "sc-1x32wa2-9 bKmKjX"})
            bot.send_message(message.chat.id, dollar)

    elif message.text.strip()=='EUR':
        response = requests.get('https://minfin.com.ua/ua/currency/eur/')
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            euro = soup.find('div', {"class": "sc-1x32wa2-9 bKmKjX"})
            bot.send_message(message.chat.id, euro)
    elif message.text.strip()=='PLN':
        response = requests.get('https://minfin.com.ua/ua/currency/pln/')
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            poland = soup.find('div', {"class": "sc-1x32wa2-9 bKmKjX"})
            bot.send_message(message.chat.id, poland)
bot.polling()