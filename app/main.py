import asyncio
from aiogram import Bot, Dispatcher
from app.config import BOT_TOKEN
from app.handlers import start, contact
from app.db.model import Base
from app.db.base import engine

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(contact.router)

    await init_db()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())