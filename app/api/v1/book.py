# -*-coding:utf-8-*-
from flask import Blueprint

from app.libs.redprint import Redprint

__author__ = 'ZeroLoo'
api=Redprint("book")

@api.route('/get')
def get_book():
    return "get book"