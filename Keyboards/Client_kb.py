from emoji import emojize
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


b1 = KeyboardButton(emojize('/Режим_работы :timer_clock:'))
b2 = KeyboardButton(emojize('/Расположение :sport_utility_vehicle:'))
b3 = KeyboardButton(emojize('/Весь_список_процедур :money_with_wings:'))
b4 = KeyboardButton(emojize('Поделиться номером :telephone:'), request_contact=True)
b5 = KeyboardButton(emojize('/Контакты :writing_hand_medium-light_skin_tone:'))
b6 = KeyboardButton(emojize('/Весь_прайс :heavy_dollar_sign:'))


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).insert(b2).add(b3).add(b4).add(b5).insert(b6)

