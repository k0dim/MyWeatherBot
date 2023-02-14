import logging
import configparser

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext

import App.handler.inline_keyboard as ik
import App.handler.messages as mes
from App.database.db_settings import DBweather
from App.handler.coordinate_text import get_coordinat

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
logger.error("Starting bot")

configs = configparser.ConfigParser()
configs.read('config.ini')

db = DBweather()

bot = Bot(token=configs['APIKEY']['APIKEY_BOT'])
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def send_location(message: types.Message, state: FSMContext):
    await message.answer(text=f'Hi @{message.chat.username}!\n' \
                                'I can tell you the current weather!\n' \
                                'Write the name of the city ✏️\n' \
                                'Or send your geolocation using the button below 📍',
                        reply_markup=ik.LOCATION)


@dp.message_handler(content_types=[types.ContentType.LOCATION])
async def get_location(message: types.Location, state: FSMContext):
    if not db.search_user(message.chat.id):
        db.insert(
            id=message.chat.id,
            username=message.chat.username,
            latitude = message.location['latitude'],
            longitude = message.location['longitude']
        )
    else:
        db.update(
            id=message.chat.id,
            latitude = message.location['latitude'],
            longitude = message.location['longitude']
        )
    await bot.send_message(chat_id=message.chat.id, text=mes.weather(message.chat.id),
                            reply_markup=ik.WEATHER)


@dp.message_handler()
async def get_location_text(message: types.Message, state: FSMContext):
    try:
        coordinate = get_coordinat(str(message.text))
        if not db.search_user(message.chat.id):
            db.insert(
                id=message.chat.id,
                username=message.chat.username,
                latitude = coordinate['latitude'],
                longitude = coordinate['longitude']
            )
        else:
            db.update(
                id=message.chat.id,
                latitude = coordinate['latitude'],
                longitude = coordinate['longitude']
            )
        await bot.send_message(chat_id=message.chat.id, text=mes.weather(message.chat.id),
                                reply_markup=ik.WEATHER)
    except:
        await bot.send_message(chat_id=message.chat.id, text=f'Location "{message.text}" not found\n'
                                                                'Please correct your request.\n')


@dp.message_handler(commands=['weather'])
async def show_weather(message: types.Message):
    await message.answer(text=mes.weather(message.chat.id),
                        reply_markup=ik.WEATHER)


@dp.message_handler(commands=['hepl'])
async def show_hepl_message(message: types.Message):
    await message.answer(text=f'This bot can get the current weather from your location.',
                        reply_markup=ik.HELP)


@dp.message_handler(commands=['wind'])
async def show_wind(message: types.Message):
    await message.answer(text=mes.wind(message.chat.id),
                        reply_markup=ik.WIND)


@dp.message_handler(commands=['sun_time'])
async def show_wind(message: types.Message):
    await message.answer(text=mes.sun_time(message.chat.id),
                        reply_markup=ik.SUN_TIME)


@dp.callback_query_handler(text='weather')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=mes.weather(callback_query["from"]["id"]),
        reply_markup=ik.WEATHER
    )


@dp.callback_query_handler(text='wind')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=mes.wind(callback_query["from"]["id"]),
        reply_markup=ik.WIND
    )


@dp.callback_query_handler(text='sun_time')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=mes.sun_time(callback_query["from"]["id"]),
        reply_markup=ik.SUN_TIME
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)