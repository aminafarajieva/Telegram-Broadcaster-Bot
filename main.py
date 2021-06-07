import telebot
API_KEY = "1804620476:AAGMtGpjwR4CQgbrhzAZlKwaxr-5rmOpeZg" #needed to change by your own bot token
bot = telebot.TeleBot(API_KEY)

f = open('contacts.txt','r')
users = set()
for i in f:
    users.add(i.strip())
f.close()

# приветствует и добавляет юзера в список юзеров
@bot.message_handler(commands=['start'])
def welcome(message):
    id = message.chat.id
    if not str(id) in users:
        f = open('contacts.txt','a')
        f.write(str(id)+'\n')
        users.add(id)
    bot.send_message(id, 'Welcome to "' + str(bot.get_me().first_name) + '"!\nYou will receive a remainder everyday.',parse_mode='html')

# рассылает всем юзерам в списке текст после первого пробела
@bot.message_handler(commands=['send'])
def rassylka(message):
    for i in users:
        bot.send_message(i,message.text[message.text.find(' ')::])
bot.polling()