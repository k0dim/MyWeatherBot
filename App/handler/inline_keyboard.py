from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup \
    ,ReplyKeyboardMarkup, KeyboardButton


BTN_WEATHER = InlineKeyboardButton('Weather', callback_data='weather')
BTN_WIND = InlineKeyboardButton('Wind', callback_data='wind')
BTN_SUN_TIME = InlineKeyboardButton('Sunrise and sunset', callback_data='sun_time')
# LOCATION = InlineKeyboardButton('Submit your location 📍', callback_data='location')
LOCATION = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Submit your location 📍', request_location=True))


WEATHER = InlineKeyboardMarkup().add(BTN_WIND, BTN_SUN_TIME)
WIND = InlineKeyboardMarkup().add(BTN_WEATHER).add(BTN_SUN_TIME)
SUN_TIME = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND)
HELP = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND).add(BTN_SUN_TIME)

