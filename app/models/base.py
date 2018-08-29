# -*-coding:utf-8-*-
from sqlalchemy import Column, Integer, SmallInteger
from flask_sqlalchemy import SQLAlchemy

__author__ = 'ZeroLoo'

db = SQLAlchemy()


class Base(db.Model):
    carete_time = Column("create_time", Integer)
    status = Column(SmallInteger, default=1)
