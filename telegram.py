import telebot

"""API_KEY = os.getenv('API_KEY')
print("BOT TOKEN --> " + str(API_KEY))
bot = telebot.TeleBot(API_KEY)
chat_id = os.getenv('CHAT_ID')"""

API_KEY = '5871023940:AAEaD45sHcXp8xtOB-ggSq6Q8RBsHWEzCf4'
bot = telebot.TeleBot(API_KEY)
chat_id = '1498114607'
nikita_chat_id = '525390336'

def createMessage(old_price, new_price, discount, url, name, our_price, our_discount, our_url):
    mesaj = "{}\n\
{}p стало {}p спп {}%\
{}\n\
Наша цена {}p - - спп {}%\n\
{}".format(name, old_price, new_price, discount, url, our_price, our_discount)
    return mesaj

@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message, "Hey! Hows it Going")

def sendNot(msg):
    bot.send_message(chat_id=chat_id,
                     text=msg,
                     parse_mode='HTML')
                    
def sendNotTest():
    msg = "TEST"
    bot.send_message(chat_id=chat_id, text= msg, parse_mode='HTML')


def main(): 
    #bot.polling()
    sendNotTest()
    
if __name__ == '__main__':
    main()