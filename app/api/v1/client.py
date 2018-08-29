# -*-coding:utf-8-*-
from app.libs.redprint import Redprint

__author__ = 'ZeroLoo'

api=Redprint('client')

api.route('/register')
def create_client():
    pass