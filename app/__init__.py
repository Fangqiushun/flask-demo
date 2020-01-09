# -*- coding: utf-8 -*-
# @Time : 2019/12/22 15:47
# @Author : Chilson

from flask import Flask
from app.api.v1 import create_blueprint_v1
from app.views import au, ind


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.register_blueprint(ind, url_prefix='/')
    app.register_blueprint(au, url_prefix='/auth')
    for bp in create_blueprint_v1():
        app.register_blueprint(bp, url_prefix='/v1')
    return app
