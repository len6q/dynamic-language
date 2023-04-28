from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import random

API_TOKEN = '6297184090:AAHbEfaN1p1EYP6mrb9co5w3id0_Zv80MDY'
IMAGES_PATH = 'lab2/images/{}.jpg'
BUTTON_TEXT = 'Получить мотивацию'

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    item = KeyboardButton(BUTTON_TEXT)
    markup.add(item)
    await message.answer('Привет!\nХочешь получить немного мотивации?', reply_markup=markup)

@dp.message_handler(lambda mes: mes.text and BUTTON_TEXT.lower() in mes.text.lower())
async def get_motivation(message: Message):
    with open(get_image_path(), 'rb') as photo:
        await message.answer_photo(photo)    

def get_image_path():
    random_index = random.randint(1, 24)
    return IMAGES_PATH.format(random_index)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)