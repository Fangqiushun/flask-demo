# -*- coding: utf-8 -*-
# @Time : 2019/12/22 15:52
# @Author : Chilson

from flask import request
from app.utils.greenprint import Greenprint
from app.utils.md5 import md5
from app.utils.sqlhelper import fetch_one
from app.utils.error_code import Success, AuthFailed
from app.forms.forms import LoginForm

api = Greenprint('auth')


@api.route('/login', methods=['POST'])
def login():
    form = LoginForm(request.form)
    form = form.validate_for_api()
    4/0
    # 表单验证通过验证用户信息
    username = form.data.get('username')
    password = form.data.get('password')
    # md5加密
    pwd_md5 = md5(password)
    data = fetch_one('select id, nickname from userinfo where user = %s and pwd = %s', (username, pwd_md5))
    if data:
        return Success()
    else:
        return AuthFailed()