import telebot

"""API_KEY = os.getenv('API_KEY')
print("BOT TOKEN --> " + str(API_KEY))
bot = telebot.TeleBot(API_KEY)
chat_id = os.getenv('CHAT_ID')"""

API_KEY = '5871023940:AAEaD45sHcXp8xtOB-ggSq6Q8RBsHWEzCf4'
bot = telebot.TeleBot(API_KEY)
chat_id = '1498114607'
zafer_chat_id = '525390336'

def createMessage(old_price, not_disc_old, not_disc_newPrice, new_price, url, keke, name, our_price, our_url, our_kekePerc, not_disc_our):
    mesaj = "{}\n\
{}p {}p стало {}p {}p спп {}%\
{}\n\
Наша цена {}p {}p спп {}%\n\
{}".format(name, not_disc_old, old_price, not_disc_newPrice, new_price, keke, url, not_disc_our, our_price, our_kekePerc, our_url)
    return mesaj

@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message, "Hey! Hows it Going")

def sendNot(msg):
    bot.send_message(chat_id=chat_id,
                     text=msg,
                     parse_mode='HTML')
    bot.send_message(chat_id=zafer_chat_id,
                     text=msg,
                     parse_mode='HTML')
                    
def sendNotTest():
    msg = "TEST"
    bot.send_message(chat_id=zafer_chat_id, text= msg, parse_mode='HTML')


def main(): 
    #bot.polling()
    sendNotTest()
    
if __name__ == '__main__':
    main()