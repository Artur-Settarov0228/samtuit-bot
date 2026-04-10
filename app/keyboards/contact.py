from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Raqam yuborish", request_contact=True)]
    ],
    resize_keyboard=True
)