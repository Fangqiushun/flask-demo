#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 14:12
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

from app.utils.errors import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    error_code = 1


class ServerError(APIException):
    code = 500
    error_code = 999
    msg = 'sorry, we made a mistake !'


class ParameterException(APIException):
    code = 400
    error_code = 1000
    msg = 'invalid parameter'


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found'
    error_code = 1001


class Forbidden(APIException):
    code = 403
    error_code = 1002
    msg = 'forbidden, not in scope'


class ClientTypeError(APIException):
    code = 400
    error_code = 1003
    msg = 'client is invalid'


class AuthFailed(APIException):
    code = 401
    error_code = 1004
    msg = 'authorization failed'
