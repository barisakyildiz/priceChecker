import telebot
from time import sleep

"""API_KEY = os.getenv('API_KEY')
print("BOT TOKEN --> " + str(API_KEY))
bot = telebot.TeleBot(API_KEY)
chat_id = os.getenv('CHAT_ID')"""

API_KEY = ''
bot = telebot.TeleBot(API_KEY)
chat_id = ''

def createMessage(old_price, not_disc_old, not_disc_newPrice, new_price, url, keke, name, our_price, our_url, our_kekePerc, not_disc_our):
    mesaj = "{}\n\
{} {} стало {} {} спп {}%\
{}\n\
Наша цена {} {} спп {}%\n\
{}".format(name, not_disc_old, old_price, not_disc_newPrice, new_price, keke, url, not_disc_our, our_price, our_kekePerc, our_url)
    return mesaj

def createOurMessage(our_name, our_old_without_disc, our_old_with_disc, our_new_without_disc, our_new_with_disc, our_keke, our_url):
    mesaj = "{}\n\
{} {} стало {} {} спп {}%\
{}\n".format(our_name, our_old_without_disc, our_old_with_disc, our_new_without_disc, our_new_with_disc, our_keke, our_url)
    return mesaj

def createOtherMessage(name, without_disc, with_disc, keke, url):
    mesaj = "{}\n\
{} {} спп {}%\n\
{}\n".format(name, without_disc, with_disc, keke, url)
    return mesaj

@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message, "Hey! Hows it Going")

def sendNot(msg):
    try:
        bot.send_message(chat_id=chat_id, text=msg, parse_mode='HTML'); sleep(1)
    except Exception as e:
        pass

def sendNotTest():
    msg = "DO NOT CARE THE BEFORE MESSAGES"
    bot.send_message(chat_id=chat_id, text= msg, parse_mode='HTML')


def main(): 
    #bot.polling()
    sendNotTest()
    
if __name__ == '__main__':
    main()