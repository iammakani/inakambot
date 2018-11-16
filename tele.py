import requests
import re
import random
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

TOKEN=''
proxies = {
    'proxy_url': 'https://46.55.161.132:32377',
}
def holidays():
    s = 'Нет повода не выпить, друзья!!!\n\n'
    friend_list = ['Айдарика',
                   'Елену',
                   'Макса',
                   'Реныча',
                   'Мишаню',
                   'Димаса',
                   'Юлию',
                   'Данила',
                   'Борисыча',
                   'Виталю'
    ]
    r = requests.get ('http://www.calend.ru/holidays/')
    data = r.text
    out = re.findall(r'<a  href="/holidays/\d{1,5}/\d{1,5}/\d{1,5}/">(\D{1,})</a>&nbsp;',data)
    for index in out:
        s = s + 'Поздравим с праздником "'+str(index)+'" '+(random.choice(friend_list))+'!'+'\n'+'\n'
    return s

updater = Updater(TOKEN, request_kwargs=proxies)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def holi(bot, update):
    hh=holidays()
    bot.send_message(chat_id=update.message.chat_id, text=hh)

start_handler = CommandHandler('holi', holi)
dispatcher.add_handler(start_handler)

def drink(bot, update):
    friend_list = ['Айдарик и приглашает всех на склад!',
                   'Елена и зовет всех в бухгалтерию! Заодно там с автоплатежом разберемся на картах мир!',
                   'Макс и приглашает всех в эту ночь на тех этаж! Заодно коммутатор заменим на кольце!',
                   'Ринат...только сначала надо опоры посчитать...',
                   'Мишаня и зовет всех в серверную, шатать кластера РТУ!',
                   'Юлия и зовет всех в админскую. Там весело! И холодно...',
                   'Димас и зовет всех в Ишимбай...хотя не,...в Салават...или в Ишимбай?...хотя не, в Уфу...хотя погодите...',
                   'Борисыч и зовет всех в Стерлик - в боулинг! Катаем шары, а не вату!'
                   ]
    mes = f'За выпивку сегодня платит {(random.choice(friend_list))}'
    bot.send_message(chat_id=update.message.chat_id, text=mes)

drink_handler = CommandHandler('drink', drink)
dispatcher.add_handler(drink_handler)

updater.start_polling()


