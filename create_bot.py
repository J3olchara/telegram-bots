from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = "5245666893:AAGwJqNQ0oR5_tMaiG4XgxWaNU0g-Ard0Pc"
#BOT_URL = 'https://melodydotobot.herokuapp.com/'
bot = Bot(token=(TOKEN))
dp = Dispatcher(bot, storage=storage)