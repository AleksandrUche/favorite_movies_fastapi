import httpx
from fastapi import HTTPException, status

from core.settings import BASE_URL_KINOPOISK, API_KEY_KINOPOISK


class KinopoiskAPIClient:
    def __init__(self, url: str = BASE_URL_KINOPOISK):
        self.url_kinopoisk = url

    async def search_movie(self, keyword: str, page: int = 1):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    self.url_kinopoisk + '/api/v2.1/films/search-by-keyword',
                    params={'keyword': keyword, 'page': page},
                    headers={
                        'X-API-KEY': API_KEY_KINOPOISK,
                        'Content-Type': 'application/json'},
                )
                response.raise_for_status()
                data = response.json()

                if not data['searchFilmsCountResult']:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail='Фильм не найден'
                    )

                return data

            except httpx.HTTPStatusError as exc:
                raise HTTPException(
                    status_code=exc.response.status_code,
                    detail=str(exc)
                )

    async def detail_movies(self, movie_id: int):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    self.url_kinopoisk + f'/api/v2.2/films/{movie_id}',
                    headers={
                        'X-API-KEY': API_KEY_KINOPOISK,
                        'Content-Type': 'application/json'},
                )
                response.raise_for_status()

                return response.json()

            except httpx.HTTPStatusError as exc:
                raise HTTPException(
                    status_code=exc.response.status_code,
                    detail=str(exc)
                )
