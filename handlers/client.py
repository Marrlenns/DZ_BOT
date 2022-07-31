from aiogram import types, Dispatcher
import random
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from config import dp, bot
from database.bot_db import sql_command_random
from parser import news


async def bot_mem(message: types.Message):
    lst = ["media/sherlok.jpg", "media/bot_mem.png", "media/nigga_mem.jpg"]
    photo = open(random.choice(lst), 'rb')
    await bot.send_photo(message.chat.id, photo=photo)

async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.reply("Надо ответить на сообщение🙄")
# @dp.message_handler(commands=['quiz'])
async def quiz_handler(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data='button_1')
    markup.add(button_1)

    question = "Какое самое лучшее аниме?"
    answers = ['Черный клевер', 'Наруто', 'Тетрадь смерти', 'Хвост феи', 'Хантер х Хантер']

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Бог Шиноби",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

async def show_random_food(message: types.Message):
    await sql_command_random(message)

async def parser_news(message: types.Message):
    data = news.parser()
    for item in data:
        await bot.send_message(
            message.from_user.id,
            f"{item['title']}\n\n"
            f"{item['Companytitle']}\n"
            f"{item['upper']}"
        )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(bot_mem, commands=['mem'])
    dp.register_message_handler(quiz_handler, commands=['quiz'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(show_random_food, commands=['random'])
    dp.register_message_handler(parser_news, commands=['news'])