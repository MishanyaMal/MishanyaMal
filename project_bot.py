import webbrowser
import requests
import telebot

token = '8146333746:AAFw-Jj-BghNwORJ5PUQg8bPFEwMtcDoTGg'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Let's find an old website.\n"
                          "Type </show> a website URL and a year, month, and day, like 20150613: ")

@bot.message_handler(commands=['show'])
def show(message):
    args = message.text.split(' ', 2)
    if len(args) < 3:
        bot.reply_to(message, 'Try again')
        return
    site, era = args[1], args[2]
    url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
    response = requests.get(url)
    data = response.json()
    try:
        old_site = data["archived_snapshots"]["closest"]["url"]
        bot.reply_to(message, f'Found this copy: {old_site}\n'
                              f'It should appear in your browser now.')
        webbrowser.open(old_site)
    except:
        bot.reply_to(message, f"Sorry, no luck finding {site}")

bot.polling(none_stop=True)