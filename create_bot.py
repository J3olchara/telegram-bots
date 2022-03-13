from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = "YOUR BOT TOKEN"
#BOT_URL = 'YOUR BOT URL'
bot = Bot(token=(TOKEN))
dp = Dispatcher(bot, storage=storage)
