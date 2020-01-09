# -*- coding: utf-8 -*-
# @Time : 2019/12/22 15:52
# @Author : Chilson

from flask import request, session
from app.utils.greenprint import Greenprint
from app.utils.md5 import md5
from app.utils.sqlhelper import fetch_one
from app.forms import LoginForm
from flask import jsonify

api = Greenprint('auth')


@api.route('/login', methods=['POST'])
def login():
    form = LoginForm(request.form)
    if form.validate():
        # 表单验证通过验证用户信息
        username = form.data.get('username')
        password = form.data.get('password')
        # md5加密
        pwd_md5 = md5(password)
        data = fetch_one('select id, nickname from userinfo where user = %s and pwd = %s', (username, pwd_md5))
        if data:
            session['user_info'] = {
                'user_id': data['id'],
                'nick_name': data['nickname']
            }
            return jsonify({'code': 200, 'data': {'msg': '登录成功'}})
        else:
            return jsonify({'code': 200, 'data': {'errmsg': '用户名或账号不正确'}})
    return jsonify({'code': 200, 'data': {'errmsg': form.errors}})