from typing import Optional, List

from fastapi import HTTPException, status
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.my_movies.models import FavoriteMoviesOrm
from app.my_movies.schemas import FavoriteMoviesRequestDTO
from app.user.schemas import UserDTO


async def add_movie(
    request_data: FavoriteMoviesRequestDTO,
    current_user: UserDTO,
    session: AsyncSession,
) -> Optional[FavoriteMoviesOrm]:
    """Добавляет фильм в избранное"""
    db_item = FavoriteMoviesOrm(
        kinopoisk_id=request_data.kinopoisk_id,
        title=request_data.title,
        user_id=current_user.id
    )
    session.add(db_item)
    await session.commit()
    await session.refresh(db_item)
    return db_item


async def get_movies_user(
    current_user: UserDTO,
    session: AsyncSession,
) -> List[FavoriteMoviesOrm] | HTTPException:
    """Возвращает все избранные фильмы пользователя"""
    stmt = select(FavoriteMoviesOrm).filter(
        FavoriteMoviesOrm.user_id == current_user.id)
    res = await session.scalars(stmt)
    movies = res.all()
    if not movies:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="У вас нет избранных фильмов."
        )
    return movies


async def remove_movie(
    kinopoisk_id: int,
    current_user: UserDTO,
    session: AsyncSession,
) -> None:
    """Удаляет фильм из избранного"""
    stmt = delete(FavoriteMoviesOrm).filter(
        FavoriteMoviesOrm.user_id == current_user.id,
        FavoriteMoviesOrm.kinopoisk_id == kinopoisk_id,
    )
    res = await session.execute(stmt)

    if res.rowcount == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Фильм с указанным id не найден в избранном"
        )

    await session.commit()
