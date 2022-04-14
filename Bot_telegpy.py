from aiogram.utils import executor
from Create_bot import dp
from data_base import sqlite_db


async def on_startup(_):
    print('Бот вошел в онлайн')
    sqlite_db.sql_start()


from Handlers import Client, Admin, Other


Client.register_handlers_client(dp)
Admin.register_handlers_admin(dp)
Other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
