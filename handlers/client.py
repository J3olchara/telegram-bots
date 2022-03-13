from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboard import ClientButtons
from aiogram.dispatcher.filters import Text
from database import sqlite_db
from database.sqlite_db import sql_readlines
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Привет, хочешь расскажу тебе о melody?", reply_markup = ClientButtons)
        await message.delete()
    except:
        await message.reply("Я не могу написать тебе потому что ты не начал общение со мной.\n напиши мне /start https://t.me/melodydotobot")
async def coachvk(message: types.Message):
    await bot.send_message(message.from_user.id, "вк тренера: https://vk.com/h3lladreams")
async def getbio(message: types.Message):
    photo = open('biophoto.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo = photo, caption = "Эдгар «melody» Стуров (ММР: 8500) — dota 2 personal coach / ex-pro-player\n\nПривет! Меня зовут Эдгар, мне 21 год мой игровой ник: 'melody', ММР - 8500 (TOP 150 EU) Тренировки провожу только я!\n\nВ Dota 2 играю с 2013 года и имею 20.000+ часов в игре, основная роль - Керри, обучаю все позиции, если ваш рейтинг < 7.000 ММР\n\n📌 В первую очередь я - игрок с огромным опытом и багажом знаний как в компететив Dota, так и в бусте и прокачке аккаунтов. Я прошел очень длинный путь в мире Dota 2 и своим опытом хочу поделиться с вами!\n\nТак же являюсь ex-PRO-игроком, играл под тегом следующих организаций:\nGMT Esports\nImperial Pro Gaming\nMagic Hands\nWINside eSports\n✅ Тренерством занимаюсь больше 3-ех лет ✅ Опыт работы - 300+ учеников ✅ 100+ отзывов о моей работе.\n\n🏆 За весь свой экспирианс в сфере обучения, я вывел самую эффективную систему тренировок, которая помогает игрокам от 0 до 7500 ММР повышать свой скилл и ММР.\n\nДля меня важен ваш результат, поэтому каждый клиент получается индивидуальный подход и систему обучения.\n\n")
    await bot.send_message(message.from_user.id, "Цель моего тренировочного курса:\n\n📌 1. Выявить ваши ключевые ошибки и помочь их исправить\n\n📌 2. Усилить лейнининг и его сопутствующие\n\n📌 3. Поставить правильный макро скилл и улучшить передвижения по карте\n\n📌 4. Передать майндсет и понимание, которое поможет в долгосрочной перспективе\n\n📌 5. Психологическая помощь (борьба с тильтом, настроем на игры и т.д.)")
async def getreviews(message: types.Message):
    await bot.send_message(message.from_user.id, 'Отзывы учеников — https://vk.com/topic-182008803_41701179')
async def getServicesDescription(message: types.Message):
    lines = await sqlite_db.sql_readlines()
    for service in lines:
        await bot.send_photo(message.from_user.id, service[0], f'{service[1]}\nОписание: {service[2]}\n\nЦена: {service[3]}', reply_markup=(InlineKeyboardMarkup().\
                add(InlineKeyboardButton(text = 'Написать тренеру', url = 'https://t.me/h3lladreams'))))

        


def register_handlers_client(dp: Dispatcher): 
    dp.register_message_handler(getreviews, commands = ['отзывы'])
    dp.register_message_handler(getreviews, Text(equals = 'отзывы', ignore_case = True))
    dp.register_message_handler(commands_start, commands = ['start', 'help'])
    dp.register_message_handler(coachvk, commands = ['ВК_тренера'])
    dp.register_message_handler(coachvk, Text(equals = 'ВК тренера', ignore_case = True))
    dp.register_message_handler(getbio, commands = ['Информация_о_тренере'])
    dp.register_message_handler(getbio, Text(equals = 'Информация о тренере', ignore_case = True))
    dp.register_message_handler(getbio, Text(equals = 'Хочу', ignore_case = True))
    dp.register_message_handler(getServicesDescription, commands = ['описание_услуг'])
    dp.register_message_handler(getServicesDescription, Text(equals = 'описание услуг', ignore_case = True))



