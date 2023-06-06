import telebot
from project1 import giphy_gif

api_key = "6206705730:AAGDucqSW0Nh5vAlYvZi6N4auxvRa6TT46Q"
bot = telebot.TeleBot(api_key)

@bot.message_handler()
def answering(message):
    name = message.text
    links = giphy_gif(name)
    for link in links:
        bot.send_message(message.chat.id, f"{link}")



bot.polling(non_stop=True)