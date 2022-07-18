# from aiogram import types, Dispatcher
# from config import ADMIN, bot, dp
# import random
#
# async def game(message: types.Message):
#     if message.text.startswith('game'):
#         print(type(message.from_user.id), type(ADMIN))
#         if message.from_user.id in ADMIN:
#             emojies = ['🎯', '🎳', '🎰', '🎲', '⚽', '️🏀']
#             rand_game = random.choice(emojies)
#             await bot.send_dice(message.chat.id, emoji=rand_game)
#         else:
#             await message.reply("Эту комманду может использовать только ХОЗЯИН😤")
#
# def register_handlers_admin(dp: Dispatcher):
#     dp.register_message_handler(game)