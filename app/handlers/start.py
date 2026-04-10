from aiogram import Router
from aiogram.types import Message
from app.keyboards.contact import contact_keyboard
from app.services.user_service import get_user_by_tg

router = Router()

@router.message(lambda m: m.text == "/start")
async def start_handler(message: Message):
    user = await get_user_by_tg(message.from_user.id)

    if user:
        await message.answer("Siz allaqachon ro‘yxatdan o‘tgansiz ✅")
    else:
        await message.answer(
            "Telefon raqamingizni yuboring:",
            reply_markup=contact_keyboard
        )