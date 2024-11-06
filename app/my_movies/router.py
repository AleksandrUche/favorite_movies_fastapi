from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_session
from app.my_movies.schemas import (
    FavoriteMoviesRequestDTO,
    FavoriteMoviesResponseDTO,
)
from app.my_movies.services import service, api_kinopoisk
from app.user.schemas import UserDTO
from app.user.services.security import get_current_user

router = APIRouter()


@router.get('/search', summary='Поиск фильма по названию', tags=['Kinopoisk API'])
async def search_movies(
    keyword: str, page: int = 1, current_user: UserDTO = Depends(get_current_user),
):
    client = api_kinopoisk.KinopoiskAPIClient()
    return await client.search_movie(keyword, page)


@router.get(
    '/favorites',
    response_model=List[FavoriteMoviesResponseDTO],
    summary='Избранные фильмы пользователя',
    tags=['movies'],
)
async def get_favorites_movies(
    current_user: UserDTO = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    return await service.get_movies_user(current_user, session)


@router.get(
    '/{kinopoisk_id}',
    summary='Детальный данные фильма',
    description='Ищет фильм по kinopoisk_id',
    tags=['Kinopoisk API'],
)
async def detail_movie(
    kinopoisk_id: int, current_user: UserDTO = Depends(get_current_user),
):
    client = api_kinopoisk.KinopoiskAPIClient()
    return await client.detail_movies(movie_id=kinopoisk_id)


@router.post(
    '/favorites',
    status_code=status.HTTP_201_CREATED,
    summary='Добавить фильм к себе в избранное',
    tags=['movies']
)
async def add_favorite_movie(
    request: FavoriteMoviesRequestDTO,
    session: AsyncSession = Depends(get_session),
    current_user: UserDTO = Depends(get_current_user),
):
    return await service.add_movie(request, current_user, session)


@router.delete(
    '/favorites/{kinopoisk_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    summary='Удаление фильма из избранного',
    tags=['movies'],
)
async def remove_favorite_movie(
    kinopoisk_id: int,
    current_user: UserDTO = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    return await service.remove_movie(kinopoisk_id, current_user, session)
