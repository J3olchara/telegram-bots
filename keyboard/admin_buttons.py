from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

newservice = KeyboardButton('Загрузить услугу')
cancelhandler = KeyboardButton('отмена')
backtoclient = KeyboardButton('клиентский режим')
services = KeyboardButton('Услуги')

ServisesDescription = KeyboardButton('Описание услуг')
AboutCoach = KeyboardButton('Информация о тренере')
reviews = KeyboardButton('Отзывы')
adminbutton = KeyboardButton('Режим редактирования')


AdminButtons = ReplyKeyboardMarkup(resize_keyboard = True).row(newservice,services, backtoclient).add(cancelhandler)
AdminCommand = ReplyKeyboardMarkup(resize_keyboard = True).row(AboutCoach, ServisesDescription).add(reviews, adminbutton)
















