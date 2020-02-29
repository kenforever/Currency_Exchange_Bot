from telegram.ext import Updater, CommandHandler
import urllib.request
import json

def exchange(update, context):
    cur_from = str.upper(update.message.text[10:13])
    cur_to = str.upper(update.message.text[14:17])
    amount = int(update.message.text[18:])
    url = ('https://api.exchangerate-api.com/v4/latest/'+cur_from)
    html = urllib.request.urlopen(url)
    hjson = json.loads(html.read()) 
    ans = amount * round(hjson['rates'][cur_to],6)
    update.message.reply_text('把{}{}換到{}有{}元。'.format(amount, cur_from, cur_to, ans))

updater = Updater('token', use_context=True)

updater.dispatcher.add_handler(CommandHandler('exchange', exchange))
updater.start_polling()
updater.idle()
