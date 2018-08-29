# -*-coding:utf-8-*-
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm

__author__ = 'ZeroLoo'

api=Redprint('client')

api.route('/register')
def create_client():
    data=request.json
    form=ClientForm(data=data)
    if form.validate():
        promise={
            ClientTypeEnum.USER_EMAIL:__register_user_by_email
        }

def __register_user_by_email(form):
    User.register_by_email(form.account.data,form.secret.data)