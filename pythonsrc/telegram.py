import os
import telebot

"""API_KEY = os.getenv('API_KEY')
print("BOT TOKEN --> " + str(API_KEY))
bot = telebot.TeleBot(API_KEY)
chat_id = os.getenv('CHAT_ID')"""

API_KEY = '5871023940:AAEaD45sHcXp8xtOB-ggSq6Q8RBsHWEzCf4'
bot = telebot.TeleBot(API_KEY)
chat_id = '1498114607'

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hey! Hows it Going")

@bot.message_handler(commands=['Sa'])
def sendNot(message):
    bot.send_message(chat_id=chat_id,
                     text="Test Notification",
                     parse_mode='HTML')

def main():
    bot.polling()
    sendNot()

if __name__ == '__main__':
    main()