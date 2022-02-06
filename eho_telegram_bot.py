import telebot
# create bot example
bot = telebot.TeleBot('5158869077:AAGEo8h9-RhjO6DyJmvpcb27vR3dTXkxnAE')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я вас слушаю. Напиши мне что-нибудь )')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

# Запускаем бота
bot.polling(none_stop=True, interval=0)
