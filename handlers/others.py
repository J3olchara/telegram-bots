from aiogram import types, Dispatcher
import json, string
from create_bot import dp

async def echo_send(message: types.Message):
    if message.text.capitalize() == "Привет":
        await message.answer("Привет я могу рассказать тебе о melody, ты хочешь?")
    else:
       await message.reply("Я не знаю что на это ответить")
    #await bot.send_message(message.from_user.id, message.text)

def register_handlers_others(dp: Dispatcher):
    dp.register_message_handler(echo_send)