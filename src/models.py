from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, ForeignKey

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    
    favorites: Mapped[list["Favorite"]]= relationship(back_populates="user")


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,

        }
    
class Character(db.Model):
    __tablename__ = 'characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    name_characeter:  Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    gender: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    hair: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    favorites: Mapped[list["Favorite"]] = relationship(back_populate="characters")


    def serialize(self):
        return {
            "id": self.id,
            "name_characeter": self.name_characeter,
            "gender": self.gender,
            "hair": self.hair,
        }


class Planet (db.Model):
    __tablename__ = 'planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    name:  Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    climate: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    population : Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    favorites: Mapped[list["Favorite"]] = relationship(back_populate="planet")


def serialize(self):
        return {
            "id": self.id,
            "name": self.self,
            "climate": self.climate,
            "population": self.population,
        }


class Favorite(db.Model):
    __tablename__ = 'favorite'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    planet_id:  Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=True)
    character_id:  Mapped[int] = mapped_column(ForeignKey("character.id"),nullable=True)

    
    planet = relationship(back_populates="favorites")
    character = relationship(back_populates="favorites")
    user = relationship(back_populates="favorites")


    def serialize(self):
        return {
            "id": self.id,
            "character_id": self.image_url,
            "planet_id": self.planet_id,
            "user_id": self.user_id,
        }
