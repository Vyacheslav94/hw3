import telebot
import time
# Токен, который выдает @botfather
bot = telebot.TeleBot('5154744425:AAGrBtW4CuZ9m0RFEaWA95xan3AHXvTgCis')
# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = 'Анеки категории С'
# Загружаем список шуток
f = open('data/fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()
# Пока не закончатся шутки, посылаем их в канал
for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke)
    # Делаем паузу в один час
    time.sleep(3600)
bot.send_message(CHANNEL_NAME, "Анекдоты закончились :-(")
