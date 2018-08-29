# -*-coding:utf-8-*-
from flask import Blueprint

from app.libs.redprint import Redprint

__author__ = 'ZeroLoo'

api=Redprint("/user")
@api.route('/get')
def get_user():
    return "get user"

@api.route('/create')
def create_user():
    pass