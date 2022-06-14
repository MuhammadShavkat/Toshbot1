import logging
# from Knopka import *
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from tugma import *
from aiogram import Bot, Dispatcher, executor, types
from config import *
from weather import *
from aiogram.dispatcher.filters import BoundFilter, Command
import io
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

class AdminFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        member = await message.chat.get_member(message.from_user.id)
        return member.is_chat_admin()

class IsGroup(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        )

class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    members = ", ".join([m.full_name for m in message.new_chat_members])
    await message.reply(f"Xush kelibsiz, {members}.")


@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        if message.left_chat_member.username:
            await message.answer(f"@{message.left_chat_member.username} guruhni tark etdi")
        else:
            await message.answer(f"Nomalum shaxs guruhni tark etdi")

    elif message.from_user.id == (await bot.me).id:
        return
    else:
        await message.answer(f"{message.left_chat_member.full_name} guruhdan haydaldi "
                             f"Admin: @{message.from_user.username}.")


@dp.message_handler(IsPrivate(), Command('start', prefixes="!#$%/"))
async def send_welcome(message: types.Message):
    await message.answer("Siz botning ichidasiz!!")


@dp.message_handler(AdminFilter(), commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Salom admin!")


@dp.message_handler(IsGroup(), Command('start', prefixes="!$"))
async def send_welcome(message: types.Message):
    await message.answer("Salom siz gruppadasiz!")


@dp.message_handler(IsGroup(), Text(equals=["telba","ha onangni","ahmoq"]))
async def t1(message: types.Message):
    await message.answer("bunday soz yozmang!")


@dp.message_handler(IsGroup(), Command("set_photo", prefixes="!/"), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    #1-usul
    await message.chat.set_photo(photo=input_file)


@dp.message_handler(IsGroup(), Command("set_title", prefixes="!/"), AdminFilter())
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    #2-usul
    await bot.set_chat_title(message.chat.id, title=title)



@dp.message_handler(IsGroup(), Command("set_description", prefixes="!/"), AdminFilter())
async def set_new_description(message: types.Message):
    source_message = message.reply_to_message
    description = source_message.text
    # 1-usul
    # await bot.set_chat_description(message.chat.id, description=description)
    # 2-usul
    await message.chat.set_description(description=description)
import asyncio
import datetime
import re
import aiogram
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest


# /ro oki !ro (read-only) komandalari uchun handler
# foydalanuvchini read-only ya'ni faqat o'qish rejimiga o'tkazib qo'yamiz.
@dp.message_handler(IsGroup(), Command("ro", prefixes="!"), AdminFilter())
async def read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5

    # 5-minutga izohsiz cheklash
    # !ro 5
    # command='!ro' time='5' comment=[]

    # 50 minutga izoh bilan cheklash
    # !ro 50 reklama uchun ban
    # command='!ro' time='50' comment=['reklama', 'uchun', 'ban']

    time = int(time)

    # Ban vaqtini hisoblaymiz (hozirgi vaqt + n minut)
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    try:
        await message.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_date)
       # await message.reply_to_message.delete()
    except aiogram.utils.exceptions.BadRequest as err:
        await message.answer(f"Xatolik! {err.args}")
        return

    # Пишем в чат
    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} {time} minut yozish huquqidan mahrum qilindi.\n"
                         f"Sabab: \n{comment}")

    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")
    # 5 sekun kutib xabarlarni o'chirib tashlaymiz
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()

# read-only holatdan qayta tiklaymiz
@dp.message_handler(IsGroup(), Command("unro", prefixes="!/"), AdminFilter())
async def undo_read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False,
    )
    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")

    await asyncio.sleep(5)
    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.reply(f"Foydalanuvchi {member.full_name} tiklandi")

    # xabarlarni o'chiramiz
    await message.delete()
    await service_message.delete()

# Foydalanuvchini banga yuborish (guruhdan haydash)
@dp.message_handler(IsGroup(), Command("ban", prefixes="!"), AdminFilter())
async def ban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.kick(user_id=member_id)

    # Foydalanuvchini bandan chiqarish, foydalanuvchini guruhga qo'sha olmaymiz (o'zi qo'shilishi mumkin)
    @dp.message_handler(IsGroup(), Command("unban", prefixes="!"), AdminFilter())
    async def unban_user(message: types.Message):
        member = message.reply_to_message.from_user
        member_id = member.id
        chat_id = message.chat.id
        await message.chat.unban(user_id=member_id)
        await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} bandan chiqarildi")
        service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")

        await asyncio.sleep(5)

        await message.delete()
        await service_message.delete()

    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} guruhdan haydaldi")
    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")

    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()



@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Assalomu alaekum.kerkli kiymlar bolimi tnlang", reply_markup=asosiy_menu)



@dp.message_handler(Text(equals="Ayollar kiyimi"))
async def ayollar(message: types.Message):
    await message.delete()
    await message.answer("Ayollar kiyimlari", reply_markup=ayollar_inline_button)


@dp.message_handler(Text(equals="Erkaklar kiyimi"))
async def erkaklar(message: types.Message):
    await message.delete()
    await message.answer("Erkaklar kiyimlari", reply_markup=erkaklar_inline_button)


@dp.message_handler(Text(equals="Qizbolalar kiyimi"))
async def qizbolalar(message: types.Message):
    await message.delete()
    await message.answer("Qizbolalar kiyimlari", reply_markup=qizbolalar_inline_button)

@dp.message_handler(Text(equals="Poyafzal"))
async def poyafzallar(message: types.Message):
    await message.delete()
    await message.answer("Poyafzallar", reply_markup=Poyafzal_inline_button)


@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def sticker_handler(message:types.Message):
    await message.answer("menga sticker Yubor")

@dp.message_handler(content_types=types.ContentTypes.ANIMATION)
async def animation_handler(message:types.Message):
    await message.answer("menga animatsion Yubor")


@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def video_handler(message: types.Message):
    await message.answer("menga video Yubor")


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def location_handler(message: types.Message):
    await message.answer("menga locatsion Yubor")


@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def voice_handler(message: types.Message):
    await message.answer("menga voice Yubor")

@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def voice_handler(message: types.Message):

    my_contact = message.contact.phone_number
    await message.answer(f"Mening raqamim-{my_contact}")

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(message: types.Message):

    await message.answer(f"Yborilgan rasm{message.photo[-1].file_id}")
    await message.answer_photo(message.photo[0].file_id,"Rasm caption")



@dp.callback_query_handler(text="Andijon")
async def Shahar(call: CallbackQuery):
    res = get_weather("Andijan")
    await call.message.answer(res)


@dp.callback_query_handler(text="Navoiy")
async def Shahar(call: CallbackQuery):
    res = get_weather("Navoiy")
    await call.message.answer(res)


@dp.callback_query_handler(text="Namangan")
async def Shahar(call: CallbackQuery):
    res = get_weather("Namangan")
    await call.message.answer(res)


@dp.callback_query_handler(text="Fergana")
async def Shahar(call: CallbackQuery):
    res = get_weather("Fergana")
    await call.message.answer(res)


@dp.callback_query_handler(text="Sirdarya")
async def Shahar(call: CallbackQuery):
    res = get_weather("Sirdarya")
    await call.message.answer(res)


@dp.callback_query_handler(text="Khorezm")
async def Shahar(call: CallbackQuery):
    res = get_weather("Xorazm")
    await call.message.answer(res)


@dp.callback_query_handler(text="kadaryoadaryo")
async def Shahar(call: CallbackQuery):
    res = get_weather("Kashkadaryo")
    await call.message.answer(res)


@dp.callback_query_handler(text="Surkhandaryo")
async def Shahar(call: CallbackQuery):
    res = get_weather("Surkhandaryo")
    await call.message.answer(res)


@dp.callback_query_handler(text="Korakalpogiston")
async def Shahar(call: CallbackQuery):
    res = get_weather("Korakalpogiston")

    await call.message.reply(res)


# @dp.message_handler()
# async def echo(message: types.Message):
#     res = get_weather(message.text)
#     if res is not None:
#         await message.answer(res)
#     else:
#         await message.answer("Bunday shahar yo'q")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
