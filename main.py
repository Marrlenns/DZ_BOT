from aiogram.utils import executor
from config import dp
import logging

from handlers import client, extra, callback, admin, fsmAdminMenu

fsmAdminMenu.register_handlers_fsmAdminMenu(dp)
client.register_handlers_client(dp)
# extra.register_handlers_extra(dp)
callback.register_handlers_callback(dp)
# admin.register_handlers_admin(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
