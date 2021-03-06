#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 14:12
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

import json
from flask import request
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    """自定义API异常"""
    code = 500
    msg = 'sorry, we made a mistake!'
    error_code = 500

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(APIException, self).__init__(msg, None)

    # 将返回值定义为json格式
    def get_body(self, environ=None):
        body = dict(
            code=self.code,
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + ' ' + self.get_url_no_param()
        )
        text = json.dumps(body)
        return text

    # 告诉浏览器返回的是json格式，按照json格式解析
    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]
