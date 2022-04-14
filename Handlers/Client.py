from aiogram import types, Dispatcher
from Create_bot import dp, bot
from Keyboards import kb_client
from DB import Sqlite_db




# @dp.message_handler(commands=['start', 'help']
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, '😜Привет!Я -бот-помощник администратора. Я создан,чтобы отвечать на самые частые вопросы.\n\n'
                                                     '☎️Если ты не нашел ответа на свой вопрос, позвони по номеру: 111-111\n\n'
                                                     '🚀Для начала работы нажми /start', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \n https://t.me/salon_kras_bot')


async def salon_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ежедневно с 09:00 до 23:00')


async def salon_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Улица, номер дома')

async def nail_insta_command(message : types.Message):
    await bot.send_message(message.from_user.id, '8-999-999-99-99')

# @dp.message_handler(commands=['Весь_список_процедур'])
async def salon_allproc_command(message: types.Message):
    await Sqlite_db.sql_read(message)

async def salon_allprice_command(message: types.Message):
    await bot.send_photo(message.from_user.id, 'https://i.pinimg.com/736x/d5/d8/8f/d5d88f772c67fa36a4d798ec5dfd0a03.jpg')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(salon_open_command, commands=['Режим_работы'])
    dp.register_message_handler(salon_place_command, commands=['Расположение'])
    dp.register_message_handler(salon_allproc_command, commands=['Весь_список_процедур'])
    dp.register_message_handler(nail_insta_command, commands=['Контакты'])
    dp.register_message_handler(salon_allprice_command, commands=['Весь_прайс'])
