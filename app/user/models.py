from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class UserOrm(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    favorite_movies = relationship('FavoriteMoviesOrm', back_populates='user')
