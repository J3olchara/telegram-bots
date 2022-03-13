import psycopg2 as ps
from create_bot import bot, dp
from aiogram import Dispatcher, types
import os
import sqlite3 as sq

def startdb():
    global base2, cur2
    #base2 = ps.connect(os.environ.get('DATABASE_URL'), sslmode = 'require')
    base2 = sq.connect("database.db")
    cur2 = base2.cursor()
    if base2:
        print('admin database connected')
async def sql_adminlist():
    cur2.execute('SELECT id FROM admins')
    adminlist2 = cur2.fetchall()
    adminlist = []
    for admintuple in adminlist2:
        for admin in admintuple:
            adminlist.append(admin)
    return adminlist
async def InsertAdmin(ID, username):
    cur2.execute('INSERT INTO admins(ID, username) VALUES(%s, %s)',(ID, username))
    base2.commit()
