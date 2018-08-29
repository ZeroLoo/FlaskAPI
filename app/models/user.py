# -*-coding:utf-8-*-
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash

from app.models.base import Base

__author__ = 'ZeroLoo'


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    nickname = Column(String, nullable=False)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

    @property
    def password(self):
        return self._password

    @property.setter
    def password(self,raw):
        self._password=generate_password_hash(raw)