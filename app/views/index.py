# -*- coding: utf-8 -*-
# @Time : 2020/1/2 0:16
# @Author : Chilson

from flask import Blueprint, render_template, session, redirect
from app.utils.sqlhelper import fetch_one
from app.utils.md5 import md5

ind = Blueprint('index', __name__)


@ind.before_request
def process_request():
    if not session.get('user_info'):
        return redirect('/auth/login')


@ind.route('/')
@ind.route('/index')
def index():
    md5('fds')
    data = fetch_one(
        'select id, nickname from userinfo where user = %s and pwd = %s', ('chilson', 'chilson2go'))
    return render_template('index.html')
