from app.db.base import SessionLocal
from app.db.model import User
from sqlalchemy import select

async def get_user_by_tg(telegram_id: int):
    async with SessionLocal() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()


async def create_user(telegram_id: int, phone: str):
    async with SessionLocal() as session:
        user = User(telegram_id=telegram_id, phone=phone)
        session.add(user)
        await session.commit()