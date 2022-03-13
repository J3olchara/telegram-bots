import psycopg2 as ps
from create_bot import bot, dp
from aiogram import Dispatcher, types
import os

def startdb():
    global base, cur
    #base = ps.connect(os.environ.get('DATABASE_URL'), sslmode = 'require')
    base = sq.connect("database.db")
    cur = base.cursor()
    if base:
        print('database connected')
async def dbInsertService(state, servicedata): 
    servicedata = list(servicedata.values())
    servicephoto = servicedata[0]
    servicename = servicedata[1]
    servicedescription = servicedata[2]
    serviceprice = servicedata[3]
    cur.execute("INSERT INTO services(servicephoto, servicename, servicedescription, serviceprice) VALUES(%s, %s, %s, %s)", (servicephoto, servicename, servicedescription, serviceprice))
    base.commit()
#async def giveservices(message):
#    for service in sql_readlines():
#        await bot.send_photo(message.from_user.id, service[0], f'{service[1]}\nОписание: {service[2]}\n\nЦена: {service[3]}', reply_markup=(InlineKeyboardMarkup().\
#                add(InlineKeyboardButton(text = 'Связь с тренером', url = 'https://t.me/h3lladreams')))))
    base.commit()
async def sql_readlines():
    cur.execute('SELECT * FROM services')
    allservices = tuple(cur.fetchall())
    return allservices

async def sql_deleting(name):
    cur.execute('DELETE FROM services WHERE servicename = %s', (name,))
    base.commit()






#def register_callback_handlers(dp: Dispatcher):
#    dp.register_callback_query_handler(deletingService, text = '999')
