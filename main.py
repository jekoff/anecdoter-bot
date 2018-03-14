import telebot
import config
from sqlighter import SQLighter
from utils import emojize,unescape
from telebot import types

bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    reply_text = "Привет, меня зовут Бот Анекдот!:sunglasses:\n " \
                 "Я знаю очень много смешных анекдотов. :satisfied:\n" \
                 "Напиши мне /anekdot, и расскажу тебе один из них"
    bot.send_message(message.chat.id, emojize(reply_text))


@bot.message_handler(commands=['help'])
def send_help(message):
    pass


@bot.callback_query_handler(lambda t: True)
def call_inline(call):
    if call.message:
        if call.data=='anekdot':
            send_joke(call.message)


@bot.message_handler(commands=['anekdot'])
def send_joke(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Еще анекдот!", callback_data="anekdot"))
    sqlighter = SQLighter(config.DB_PATH)
    reply_text = "{0} :satisfied:".format(sqlighter.get_random_joke())
    bot.send_message(message.chat.id, unescape(emojize(reply_text)),reply_markup=keyboard)


@bot.message_handler(commands=['category'])
def send_categories(message):
    pass


@bot.message_handler(func=lambda t: True)
def send_answer_for_else(message):
    reply_text = "Прости, я еще плохо понимаю команды. Но я учусь!:books::muscle:\n" \
                 "Напиши /help, и я помогу тебе во всем разобраться"
    bot.reply_to(message, emojize(reply_text))


if __name__ == '__main__':
    bot.polling(none_stop=True)
