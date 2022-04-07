from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class User(Base):
    """ Модель Пользователя """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
