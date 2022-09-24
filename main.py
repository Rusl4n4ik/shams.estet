from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ContentType, Message
import aiogram.utils.markdown as fmt
from aiogram.utils.markdown import hlink
from aiogram.dispatcher import FSMContext
from keyboard import languages, menubtn_rus, back_rus, back_m, menubtn, lang, lang_ru
from db import check_existing, add_user

API_TOKEN = '5633019217:AAEEf24tnXByYEHBbK9hOdLljNIUqmEpuqw'

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Выберите язык / Tilni tanlang", reply_markup=languages)
    exist_user = check_existing(message.chat.id)
    if not exist_user:
        add_user(message.chat.id, message.from_user.first_name, message.from_user.username)


#####################################################################################################################


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_id(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.callback_query_handler(text='ru')
async def menu(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Главное меню: ', reply_markup=menubtn_rus)


@dp.message_handler(Text(equals="📞 Для справки"))
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=chat_id, photo='AgACAgIAAxkBAAMLYyuP78jIdvWm33bgDE9Enr4pxUUAAnvEMRtAeWFJzgwwHLDGajQBAAMCAAN4AAMpBA',
                            caption="Косметолог-ЭСТЕТИСТ | Самарканд \nНомер телефона: +998 91 187 85 86 \nТелеграмм: @shams_estet"
                            )


@dp.message_handler(Text(equals="👩‍⚕ Прайс лист"))
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=chat_id, photo='AgACAgIAAxkBAAOSYywaiAcgj_gLBLaQ0D9P9J9_bm0AAuHBMRsgAWFJ0x-tUI3yd6IBAAMCAAN5AAMpBA',
                            caption="Прайс лист процедур"
                            )


@dp.message_handler(Text(equals="📍 Наш адрес"))
async def location(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_location(chat_id=chat_id,longitude=66.926689, latitude=39.677500)
    await message.answer("📍 Наш адрес:  улица Беруни, 32 а. Клиника «Beauty Doctor», ориентир: Ипотека Банк. Напротив Вокзал Парка, Самарканд\n\nДля связи:\n☎️ +998 91 187 85 86\n👩🏼‍💻 @shams_estet")


@dp.message_handler(Text(equals="📝 Обратная связь"))
async def back(message: types.Message):
    chat_id = message.from_user.id
    insta = '📲 Instagram '
    await dp.bot.send_photo(chat_id=chat_id,
                            photo='AgACAgIAAxkBAAPLYywnjlPNLw8cAAFMtECh-CepbFdzAAIQwjEbIAFhSSgFWcMD8kufAQADAgADeAADKQQ',
                            caption="Номер телефона: +998 91 187 85 86 \nТелеграмм: @shams_estet\n" + (fmt.hlink(insta, "https://www.instagram.com/shams.estet/"))
                            )



@dp.message_handler(Text(equals="🔙 Вернутся к меню"))
async def back(message: types.Message):
    await message.answer('🔝 Главное меню', reply_markup=menubtn_rus)


@dp.message_handler(Text(equals="🇺🇿 / 🇷🇺 Изменить язык"))
async def back(message: types.Message):
    await message.answer('Выберите язык:', reply_markup=lang_ru)


@dp.message_handler(Text(equals="🇷🇺 Русский"))
async def back(message: types.Message):
    await message.answer('🔝 Главное меню', reply_markup=menubtn_rus)


###########################################################################################


@dp.callback_query_handler(text='ozb')
async def menu(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Asosiy Menyu:', reply_markup=menubtn)


@dp.message_handler(Text(equals="📍 Bizning manzil"))
async def location(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_location(chat_id=chat_id,longitude=66.926689, latitude=39.677500)
    await message.answer("📍 Manzil:  Beruniy ko'chasi, 32 a. Clinica «Beauty Doctor», orientir: Ipoteka Bank\n\nMurojat uchun:\n☎️ +998 91 187 85 86\n👩🏼‍💻 @shams_estet")




@dp.message_handler(Text(equals="📞 Murojat uchun"))
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=chat_id, photo='AgACAgIAAxkBAAMLYyuP78jIdvWm33bgDE9Enr4pxUUAAnvEMRtAeWFJzgwwHLDGajQBAAMCAAN4AAMpBA',
                            caption="Косметолог-ЭСТЕТИСТ | Самарканд \nTelefon raqam: +998 91 187 85 86 \nTelegram: @shams_estet"
                            )


@dp.message_handler(Text(equals="📝 Fikr mulohaza"))
async def back(message: types.Message):
    chat_id = message.from_user.id
    insta = '📲 Instagram '
    await dp.bot.send_photo(chat_id=chat_id,
                            photo='AgACAgIAAxkBAAPLYywnjlPNLw8cAAFMtECh-CepbFdzAAIQwjEbIAFhSSgFWcMD8kufAQADAgADeAADKQQ',
                            caption="Telefon raqam: +998 91 187 85 86 \nTelegram: @shams_estet\n" + (fmt.hlink(insta, "https://www.instagram.com/shams.estet/"))
                            )


@dp.message_handler(Text(equals="👩‍⚕ Bizning xizmatlar"))
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=chat_id, photo='AgACAgIAAxkBAAPZYywrhb3PxZyrAAHZvgEKNflaiBztAAIcwjEbIAFhSZ2AwdcaJl3dAQADAgADeQADKQQ',
                            caption="Xizmatlar narxlari:"
                            )


@dp.message_handler(Text(equals="🔙 Menyuga qaytish"))
async def back(message: types.Message):
    await message.answer('🔝 Asosiy Menyu', reply_markup=menubtn)


@dp.message_handler(Text(equals="🇺🇿 / 🇷🇺 Tilni o'zgartirish"))
async def back(message: types.Message):
    await message.answer('Tilingizni tanlang:', reply_markup=lang)


@dp.message_handler(Text(equals="🇺🇿 O'zbek"))
async def back(message: types.Message):
    await message.answer('🔝 Asosiy Menyu', reply_markup=menubtn)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
