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
    
class User(db.Model):
    __tablename__ = 'characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    name_characeter:  Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    gender: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    hair: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name_characeter": self.name_characeter,
            "gender": self.gender,
            "hair": self.hair,
        }


class Planets(db.Model):
    __tablename__ = 'planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    name:  Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    climate: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    population : Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

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
    planet_id:  Mapped[str] = mapped_column(ForeignKey("planet.id"), unique=True, nullable=False)
    character_id:  Mapped[str] = mapped_column(ForeignKey("character.id"), unique=True, nullable=False)

    user: Mapped["User"]= relationship(back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "character_id": self.image_url,
            "planet_id": self.planet_id,
            "user_id": self.user_id,
        }
