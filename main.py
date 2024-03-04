import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import wikipedia
from config import BOT_TOKEN, BOT_LANGUAGE

wikipedia.set_lang(BOT_LANGUAGE)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalomu aleykum, {message.from_user.full_name}\n"
                         f"Wiki_Botga xush kelibsiz !\n"
                         f"Siz bot orqali qiziqtirgan mavzuyingizga doir maqolani o'qishingiz mumkin")


@dp.message(Command('help'))
async def command_help_handler(message: Message):
    await message.answer("Botdan foydalanish uchun botga maqola mavzusini jo'nating")


@dp.message()
async def wiki_send_message(message: types.Message):
    try:
        response = wikipedia.summary(message.text)
        await message.answer(response)

    except:
        await message.answer("Bunday mavzuga doir maqola topilmadi 🤷‍♂...")


async def main():
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO, stream=sys.stdout)
asyncio.run(main())