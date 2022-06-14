import logging
import  asyncio
# from Knopka import *
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from tugma import *
from aiogram import Bot, Dispatcher, executor, types
from config import *
from aiogram.types import InputFile
from aiogram.types import Message
from weather import *
from aiogram.dispatcher.filters import BoundFilter, Command
import io
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
import sqlite3

from sqlite import Database

db = Database('main.db')
@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    name = message.from_user.username
    try:
       db.create_table_users()
    except:
       pass

    try:
        db.add_user(id=message.from_user.id,
                    name=message.from_user.full_name,
                    email=f"@{name}")
        count_user = db.count_users()[0]
        message = f"Bazaga @{name} qoshildi. Uning ID si {message.from_user.id}."
        message = f"Bazaga @{name} qoshildi. Bazada {count_user} bor"

        await   bot.send_message(chat_id=535894964,text=message)
    except sqlite3.IntegrityError:
        pass
@dp.message_handler(user_id=535894964,text="users")
async def  allusers(message: Message):
    users = db.select_all_users()
   # print(users[0][0])
   # await message.answer(users)
    for us in users:
       await message.answer(f"ID:{us[0]}.Username:{us[2]}")


@dp.message_handler(text="reklama", user_id=535894964)
async def send_ad_to_all(message: types.Message):
    rek_mes = message.reply_to_message.message_id
    n = 0
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        try:
            await bot.forward_message(chat_id=user_id, from_chat_id=535894964, message_id=rek_mes)
            await asyncio.sleep(0.1)
            n += 1
        except:
            pass
    await message.answer(f"Ushbu xabar {n} ta foydalanuvchiga yetib bordi.")

@dp.message_handler(text="add", user_id=535894964)
async def add_us(mes: types.Message):
    id_name = list(mes.reply_to_message.text.split())
    id_raqam = int(id_name[0])
    name = id_name[1]
    if len(id_name) == 3:
        email = id_name[2]
    else:
        email = None

    try:
        db.add_user(id_raqam, name, email)
    except sqlite3.IntegrityError:
        pass
    await mes.answer(f"{id_raqam} raqamli {name} {email}")


@dp.message_handler(text="cleanesdatabases", user_id=535894964)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")

@dp.message_handler(text="rasmlar")
async def img(message: types.Message):
    #await message.answer_photo("https://www.pngall.com/wp-content/uploads/5/Python-PNG-Clipart.png")
    #await message.answer_photo("https://www.pngall.com/wp-content/uploads/5/Python-PNG-HD-Image.png")

    await message.answer_photo(InputFile("rasmlar/images.jpg"))

   # await message.answer_photo("AgACAgIAAxkBAAEQIOdimz5QUrNhWxWdxbxmM_ej7ZUHGgACWLoxG9Pe4Egr2EThvxnuuQEAAwIAA20AAyQE")
@dp.message_handler(text="video")
async  def vid(message:types.Message):
    await message.answer_video(InputFile("videolar/video1.mp4"))

@dp.message_handler(text="gif")
async  def gifs(message:types.Message):
    await message.answer_animation("CgACAgQAAxkBAAEQIT9im0ctMnJYNb_59tMC4iaTntDQrwACVgIAAnZ7lFK1augSkTDqSCQE")

@dp.message_handler(text="loc")
async  def location(message:types.Message):
    await message.answer_location(41.305134660476426, 69.24731253013118)


@dp.message_handler(text="ovozber")
async def location(message: types.Message):
    await message.answer_poll(question="Bugungi sana",options=["1","2","3","4"])


@dp.message_handler(text="savol")
async def savol1(message: types.Message):
    await message.answer_poll(question="Bugungi sana",options=["1","2","3","4"],type="quiz", correct_option_id=2,is_anonymous=False)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
