from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

ServisesDescription = KeyboardButton('Описание услуг')
AboutCoach = KeyboardButton('Информация о тренере')
reviews = KeyboardButton('Отзывы')

ClientButtons = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = False)

ClientButtons.row(AboutCoach, ServisesDescription).add(reviews)
