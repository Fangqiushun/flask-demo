# -*- coding: utf-8 -*-
# @Time : 2020/1/2 0:16
# @Author : Chilson

from flask import Blueprint, render_template, session, redirect

ind = Blueprint('index', __name__)


@ind.before_request
def process_request():
    if not session.get('user_info'):
        return redirect('/auth/login')


@ind.route('/')
@ind.route('/index')
def index():
    return render_template('index.html')
