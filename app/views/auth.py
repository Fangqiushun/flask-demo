# -*- coding: utf-8 -*-
# @Time : 2020/1/5 11:02
# @Author : Chilson

from flask import Blueprint, request, render_template, session, redirect
from app.utils.md5 import md5
from app.utils.sqlhelper import fetch_one
from app.forms import LoginForm


au = Blueprint('auth', __name__)


@au.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'GET':
        form = LoginForm()
    else:
        # post请求验证表单
        form = LoginForm(request.form)
        if form.validate():
            # 表单验证通过验证用户信息
            username = form.data.get('username')
            password = form.data.get('password')
            # md5加密
            pwd_md5 = md5(password)
            data = fetch_one('select id, nickname from userinfo where user = %s and pwd = %s', (username, pwd_md5))
            if not data:
                error = '用户名密码错误'
            else:
                session['user_info'] = {
                    'user_id': data['id'],
                    'nick_name': data['nickname']
                }
                return redirect('/index')
    return render_template('login.html', form=form, error=error)


    # return redirect('/index')
