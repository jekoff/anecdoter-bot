import telebot
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    pass


@bot.message_handler(commands=['help'])
def send_help(message):
    pass


@bot.message_handler(commands=['anekdot'])
def send_joke(message):
    pass


@bot.message_handler(commands=['category'])
def send_categories(message):
    pass


@bot.message_handler(content_type=['text'])
def send_answer_for_text(message):
    pass


if __name__ == '__main__':
    bot.polling(none_stop=True)
