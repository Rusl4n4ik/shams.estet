from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


languages = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
languages.add(types.InlineKeyboardButton("๐ท๐บ ะ ัััะบะธะน", callback_data='ru'))
languages.add(types.InlineKeyboardButton("๐บ๐ฟ O'zbek", callback_data='ozb'))


menubtn_rus = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn3 = '๐ ะะปั ัะฟัะฐะฒะบะธ'
btn4 = '๐ ะะฐั ะฐะดัะตั'
btn5 = '๐ฉโโ ะัะฐะนั ะปะธัั'
btn6 = '๐ ะะฑัะฐัะฝะฐั ัะฒัะทั'
btn7 = "๐บ๐ฟ / ๐ท๐บ ะะทะผะตะฝะธัั ัะทัะบ"
menubtn_rus.add(btn3, btn4, btn5, btn6, btn7)


back_rus = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_ru = '๐ ะะตัะฝัััั ะบ ะผะตะฝั'
back_rus.add(back_ru)

lang_ru = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
c1 = "๐บ๐ฟ O'zbek"
c2 = "๐ท๐บ ะ ัััะบะธะน"
lang_ru.add(c1,c2,back_ru)



#############################################################################

back_m = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_btn = '๐ Menyuga qaytish'
back_m.add(back_btn)

lang = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
change1 = "๐บ๐ฟ O'zbek"
change2 = "๐ท๐บ ะ ัััะบะธะน"
lang.add(change1,change2,back_btn)

menubtn = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
btn3 = '๐ Murojat uchun'
btn4 = '๐ Bizning manzil'
btn5 = '๐ฉโโ Bizning xizmatlar'
btn6 = '๐ Fikr mulohaza'
btn7 = "๐บ๐ฟ / ๐ท๐บ Tilni o'zgartirish"
menubtn.add(btn3, btn4, btn5, btn6, btn7)

back_m = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_btn = '๐ Menyuga qaytish'
back_m.add(back_btn)