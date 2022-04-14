import sqlite3 as sq
from Create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('salon.db') #если такого нет, он создастся если есть подключится
    cur = base.cursor() #ЧАСТЬ КОТОРАЯ ЗАНИМАЕТСЯ РАБОТОЙ С ДАННЫМИ
    if base:
        print('База данных подключена')
    base.execute('CREATE TABLE IF NOT EXISTS AllPrice(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXt)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data: #открываем словарь
        cur.execute('INSERT INTO AllPrice VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM AllPrice').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена{ret[-1]}')


async def sql_read2():
    return cur.execute('SELECT * FROM AllPrice').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM AllPrice WHERE name == ?', (data,))
    base.commit()