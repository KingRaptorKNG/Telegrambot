import telebot
from telebot.types import Message
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def startcommand(msg: Message):
    bot.reply_to(msg, 'Привет')
    bot.send_message(msg.chat.id, 'Как дела?')


@bot.message_handler(content_types=['photo'])
def photocommand(msg: Message):
    bot.send_message(msg.chat.id, 'Классное фото!')
















bot.infinity_polling()