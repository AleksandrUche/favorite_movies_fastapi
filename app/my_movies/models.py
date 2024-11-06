from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class FavoriteMoviesOrm(Base):
    __tablename__ = 'favorite_movies'

    id: Mapped[int] = mapped_column(primary_key=True)
    kinopoisk_id: Mapped[int] = mapped_column(nullable=False)
    title: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)

    user = relationship('UserOrm', back_populates='favorite_movies')
