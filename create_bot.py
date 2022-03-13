from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = ""
#BOT_URL = 'https://melodydotobot.herokuapp.com/'
bot = Bot(token=(TOKEN))
dp = Dispatcher(bot, storage=storage)
