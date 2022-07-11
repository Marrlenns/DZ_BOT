from aiogram import types, Dispatcher
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import logging
import random


@dp.message_handler(commands=['mem'])
async def bot_mem(message: types.Message):
    lst = ["media/sherlok.jpg", "media/bot_mem.png", "media/nigga_mem.jpg"]
    photo = open(random.choice(lst), 'rb')
    await bot.send_photo(message.chat.id, photo=photo)

@dp.message_handler(commands=['quiz'])
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
        correct_option_id=3,
        explanation="Бог Шиноби",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

@dp.callback_query_handler(lambda call: call.data == "button_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton("NEXT", callback_data='button_2')
    markup.add(button_2)

    question = "Кто самый красивый в GeekTech?"
    answers = ['Аблай', 'Байдоолот', 'Эсен', 'Марлен', 'Вова', 'Исмет']
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Легко",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


# def register_handlers_callback(dp: Dispatcher):
#     dp.register_callback_query_handler(
#         quiz, lambda func: func.data == "button_1"
#     )
#     dp.register_callback_query_handler(
#         quiz_2, lambda func: func.data == "button_2"
#     )
#
@dp.message_handler()
async def echo(message: types.Message):
    try:
        k = int(message.text)
        await bot.send_message(message.from_user.id, k*k)
    except:
        await bot.send_message(message.from_user.id, message.text)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
