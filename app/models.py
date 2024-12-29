import datetime
from typing import List

from sqlalchemy import Integer, String, Date, Float, func, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from config import PG_DSN

from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine


engine = create_async_engine(
    PG_DSN,
)

Session = async_sessionmaker(bind=engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):

    @property
    def id_dict(self):
        return {'id': self.id}


class User(Base):
    __tablename__ = 'app_user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(72), nullable=False)
    email: Mapped[str] = mapped_column(String(72), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(72), nullable=False)

    advs: Mapped[List["Advertisement"]] = relationship(
        'Advertisement', back_populates='user', cascade='all, delete-orphan'
    )

    @property
    def dict(self):

        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,

        }

class Advertisement(Base):
    __tablename__ = 'advertisement'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    heading: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    creator: Mapped[int] = mapped_column(Integer, ForeignKey('app_user.id'), nullable=False)
    date_creation: Mapped[datetime.date] = mapped_column(Date, server_default=func.current_date())

    user: Mapped[User] = relationship(User, back_populates="advs")


    @property
    def dict(self):

        return {
            'id': self.id,
            'heading': self.heading,
            'description': self.description,
            'price': self.price,
            'creator': self.creator,
            'date_creation': self.date_creation.isoformat(),
        }


ORM_OBJECT = Advertisement | User
ORM_CLS = type[Advertisement | User]









