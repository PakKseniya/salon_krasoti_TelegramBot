from aiogram.utils import executor
from CreateBot import dp
from DB import SqliteDb


async def on_startup(_):
    print('Бот вошел в онлайн')
    SqliteDb.sql_start()


from Handlers import Client, Admin, Other


Client.register_handlers_client(dp)
Admin.register_handlers_admin(dp)
Other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
