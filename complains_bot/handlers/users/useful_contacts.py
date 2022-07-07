from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, db


@dp.message_handler(Text(equals="☎Полезные контакты"))
async def print_all_contacts(message:types.Message):
    result = db.get_white_list(message.from_user.id)
    if result[0]==0:
        await message.answer(
            """<u>Управляющая компания</u>:
    <b>Диспетчерская служба ООО «УЭР-ЮГ»</b>
    +7 4722 35-50-06
    <b>Инженеры ООО «УЭР-ЮГ»</b>
    +7 920 566-28-86
    <b>Бухгалтерия ООО «УЭР-ЮГ»</b>
    +7 4722 35-50-06
    Белгород, Свято-Троицкий 6-р, д. 15, подъезд
    №1
    <u>Телефоны для открытия ворот и
    шлагбаума</u>
    <b>Шлагбаум «Набережная»</b>
    +7 920 554-87-74
    <b>Ворота «Харьковские»</b>
    +7920 554-87-40.
    <b>Ворота «Мост»</b>
    +7 920 554-64-06
    <b>Калитка 1 «Мост»</b>
    +7 920 554-42-10
    <b>Калитка 2 «Мост»</b>
    +7 920 554-89-04
    <b>Калитка 3 «Харьковская»</b>
    +7 920 554-87-39
    <b>Калитка 4 «Харьковская»</b>
    +7 920 554-89-02
    
    <b>Охрана</b>
    +7 915 57-91-457
    
    <b>Участковый</b>
    Куленцова Марина Владимировна
    +7 999 421-53-72
            """

        )
    else:
        await message.answer(
            "🛑<b>Вы были заблокированы🚫</b>\nЧтобы разблокировать обратитесь к администратору: @o101xd")