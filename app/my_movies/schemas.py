from pydantic import BaseModel


class FavoriteMoviesRequestDTO(BaseModel):
    kinopoisk_id: int
    title: str


class FavoriteMoviesResponseDTO(BaseModel):
    id: int
    kinopoisk_id: int
    title: str
