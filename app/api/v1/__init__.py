# -*- coding: utf-8 -*-
# @Time : 2019/12/22 15:53
# @Author : Chilson

from flask import Blueprint
from app.api.v1 import auth


def create_blueprint_v1():
    """
    利用绿图注册蓝图，生成新的蓝图列表
    :return:
    """
    bp_v1 = Blueprint('v1', __name__)
    bp_v1s = []
    for gp in [auth]:
        bp_v1s.append(gp.api.register(bp_v1))
    return bp_v1s
