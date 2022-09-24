from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


languages = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
languages.add(types.InlineKeyboardButton("🇷🇺 Русский", callback_data='ru'))
languages.add(types.InlineKeyboardButton("🇺🇿 O'zbek", callback_data='ozb'))


menubtn_rus = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn3 = '📞 Для справки'
btn4 = '📍 Наш адрес'
btn5 = '👩‍⚕ Прайс лист'
btn6 = '📝 Обратная связь'
btn7 = "🇺🇿 / 🇷🇺 Изменить язык"
menubtn_rus.add(btn3, btn4, btn5, btn6, btn7)


back_rus = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_ru = '🔙 Вернутся к меню'
back_rus.add(back_ru)

lang_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
c1 = "🇺🇿 O'zbek"
c2 = "🇷🇺 Русский"
lang_ru.add(c1,c2,back_ru)



#############################################################################

back_m = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_btn = '🔙 Menyuga qaytish'
back_m.add(back_btn)

lang = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
change1 = "🇺🇿 O'zbek"
change2 = "🇷🇺 Русский"
lang.add(change1,change2,back_btn)

menubtn = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn3 = '📞 Murojat uchun'
btn4 = '📍 Bizning manzil'
btn5 = '👩‍⚕ Bizning xizmatlar'
btn6 = '📝 Fikr mulohaza'
btn7 = "🇺🇿 / 🇷🇺 Tilni o'zgartirish"
menubtn.add(btn3, btn4, btn5, btn6, btn7)

back_m = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_btn = '🔙 Menyuga qaytish'
back_m.add(back_btn)