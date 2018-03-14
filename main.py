import telebot
import config

bot = telebot.TeleBot(config.token)

if __name__ == '__main__':
    bot.polling(none_stop=True)
