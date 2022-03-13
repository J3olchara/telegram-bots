from aiogram.utils import executor
from create_bot import dp, bot
from database import sqlite_db, admins_db
from handlers import client, admin, others
import os
import create_bot

async def on_startup(dp):
    #await bot.set_webhook(create_bot.BOT_URL)
    print("БОТ ОНЛАЙН")
    
sqlite_db.startdb()
admins_db.startdb()

async def on_shutdown(dp):
    cur.close()
    base.close()
#    await bot.delete_webhook()

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
others.register_handlers_others(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
#executor.start_webhook(dispatcher = dp, 
#                       skip_updates = True, on_startup=on_startup, 
#                       on_shutdown=on_shutdown, 
#                       webhook_path = '', 
#                       host = "0.0.0.0",
#                       port = int(os.environ.get("PORT", 5000)))