from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard import AdminButtons, ClientButtons, AdminCommand
from aiogram import types
from create_bot import bot
from aiogram.dispatcher.filters import Text
from database.sqlite_db import sql_readlines, dbInsertService, sql_deleting
from database import sqlite_db
from database import admins_db
from database.admins_db import sql_adminlist, InsertAdmin
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




async def NewAdmin(message: types.Message):
    ID = message.from_user.id 
    username = message.from_user.username
    global adminlist
    adminlist = await admins_db.sql_adminlist()
    if str(ID) in adminlist:
        await bot.send_message(message.from_user.id, "Ты уже и так секси пудж, зачем тебе еще один мом?")
    else:
        await InsertAdmin(ID, username)
        await bot.send_message(message.from_user.id, "теперь ты сексуальный пудж(с момом и башером)")


async def GetAdminButtons(message: types.Message):
    userid = message.from_user.id
    adminlist = await admins_db.sql_adminlist()
    if str(userid) in adminlist:
        await bot.send_message(message.from_user.id, 'Вход в режим редактирования', reply_markup = AdminButtons)
        return adminlist
    else:
       await message.reply("Я не знаю что на это ответить")
async def GetClientButtonsBack(message: types.Message):
    adminlist = await admins_db.sql_adminlist()
    userid = message.from_user.id
    if str(userid) in adminlist:
        await bot.send_message(message.from_user.id, 'Возврат в клиентский режим', reply_markup = AdminCommand)
        return adminlist
    else:
       await message.reply("Я не знаю что на это ответить")
#async def adminview(message: types.Message):
#    userid = message.from_user.id
#    if str(userid) in adminlist:
#        await editservices(message)


class FSMAdmin(StatesGroup):
    servicephoto = State()
    servicename = State()
    servicedescription = State()
    serviceprice = State()
async def AdminStart(message: types.Message):
    userid = message.from_user.id
    adminlist = await admins_db.sql_adminlist()
    if str(userid) in adminlist:
        await FSMAdmin.servicephoto.set()
        await message.answer('Загрузи фото')
    else:
       await message.reply("Я не знаю что на это ответить")
async def CancelHandler(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    adminlist = await admins_db.sql_adminlist()
    if str(userid) in adminlist:
        currentstate = await state.get_state()
        if currentstate == None:
            return
        else:
            await state.finish()
            await message.reply('ОК')
    else:
       await message.reply("Я не знаю что на это ответить")
async def LoadPhoto(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    adminlist = await admins_db.sql_adminlist()
    if str(userid) in adminlist:
        async with state.proxy() as servicedata:
            servicedata['servisephoto'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.answer('Введи название услуги')
async def LoadName(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    adminlist = await admins_db.sql_adminlist()
    if str(userid) in adminlist:
        async with state.proxy() as servicedata:
            servicedata['servicename'] = message.text
        await FSMAdmin.next()
        await message.answer('Теперь добавь описание к услуге')
async def LoadDescription(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    adminlist = await admins_db.sql_adminlist()
    if str(userid) in adminlist:
        async with state.proxy() as servicedata:
            servicedata['servicedescription'] = message.text
        await FSMAdmin.next()
        await message.answer('Сколько будет стоить?')
async def LoadPrice(message: types.Message, state = FSMContext):
    userid = message.from_user.id
    adminlist = await admins_db.sql_adminlist()
    if str(userid) in adminlist:
        global servicedata
        async with state.proxy() as servicedata:
            servicedata['serviceprice'] = message.text
        await sqlite_db.dbInsertService(state, servicedata)
        await bot.send_message(message.from_user.id, 'Услуга добавлена')
        await state.finish()
async def adminview(message: types.Message):
    adminlist = await admins_db.sql_adminlist()
    if str(message.from_user.id) in adminlist:
        lines = await sqlite_db.sql_readlines()
        for service in lines:
            await bot.send_photo(message.from_user.id, service[0], f'{service[1]}\nОписание: {service[2]}\n\nЦена: {service[3]}')
            await bot.send_message(message.from_user.id, text = '^^^', reply_markup=(InlineKeyboardMarkup().\
                add(InlineKeyboardButton(f'Удалить {service[1]}', callback_data = f'del {service[1]}'))))
    else:
       await message.reply("Я не знаю что на это ответить")

async def servicedelete(callback: types.CallbackQuery):
    name = callback.data.replace('del ', "")
    await sqlite_db.sql_deleting(name)
    await callback.answer(text = f'Услуга {name} удалена', show_alert = True)



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(AdminStart, commands = ['Загрузить_услугу'], state = None)
    dp.register_message_handler(AdminStart, Text(equals = 'Загрузить услугу'))
    dp.register_message_handler(CancelHandler, state = "*", commands = ['отмена'])
    dp.register_message_handler(CancelHandler, Text(equals = 'отмена', ignore_case = True), state = "*")
    dp.register_message_handler(LoadPhoto, content_types = ['photo'], state = FSMAdmin.servicephoto)
    dp.register_message_handler(LoadName, state = FSMAdmin.servicename)
    dp.register_message_handler(LoadDescription, state = FSMAdmin.servicedescription)
    dp.register_message_handler(LoadPrice, state = FSMAdmin.serviceprice)
    dp.register_message_handler(NewAdmin, commands = ['me194lodqYerBd9UJlIloDYye1rRyGYUbgytu21UYgy'])
    dp.register_message_handler(NewAdmin, Text(equals = 'me194lodqYerBd9UJlIloDYye1rRyGYUbgytu21UYgy'))
    dp.register_message_handler(GetAdminButtons, commands = ['admin'])
    dp.register_message_handler(GetAdminButtons, Text(equals = 'Режим редактирования'))
    dp.register_message_handler(GetClientButtonsBack, commands = ['client'])
    dp.register_message_handler(GetClientButtonsBack, Text(equals = 'клиентский режим'))
    dp.register_message_handler(adminview, commands = ['услуги'])
    dp.register_message_handler(adminview, Text(equals = 'Услуги'))
    dp.register_callback_query_handler(servicedelete, lambda x: x.data and x.data.startswith('del '))














