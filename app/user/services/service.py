from typing import Optional

from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.user.models import UserOrm
from app.user.schemas import UserCreateDTO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def get_by_name(session: AsyncSession, name: str) -> Optional[UserOrm]:
    stmt = select(UserOrm).filter(UserOrm.name == name)
    res = await session.execute(stmt)
    return res.scalar()


async def get_user_by_id(session: AsyncSession, id: int) -> Optional[UserOrm]:
    stmt = select(UserOrm).filter(UserOrm.id == id)
    res = await session.execute(stmt)
    return res.scalar()


async def create_user(session: AsyncSession, obj_in: UserCreateDTO) -> UserOrm:
    db_obj = UserOrm(
        hashed_password=get_password_hash(obj_in.password),
        name=obj_in.name,
    )
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj


async def authenticate_user(
    session: AsyncSession,
    name: str,
    password: str,
) -> Optional[UserOrm]:
    user = await get_by_name(session, name=name)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
