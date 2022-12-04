import os
import telebot
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot('5871023940:AAEaD45sHcXp8xtOB-ggSq6Q8RBsHWEzCf4')

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hey! Hows it Going")

def main():
    bot.polling()

if __name__ == '__main__':
    main()