from aiogram import Router
from aiogram.types import Message
from app.services.user_service import create_user

router = Router()

@router.message(lambda m: m.contact is not None)
async def contact_handler(message: Message):
    phone = message.contact.phone_number
    telegram_id = message.from_user.id

    await create_user(telegram_id, phone)

    await message.answer("✅ Telefon raqamingiz saqlandi!")
    