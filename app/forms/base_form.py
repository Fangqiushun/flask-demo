#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 15:01
# @Author  : Chilson
# @Email   : qiushun_fang@126.com

from wtforms import Form
from app.utils.error_code import ParameterException


class BaseForm(Form):

    def __init__(self, data):
        # 调用父类的init方法
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self,):
        # 调用父类的验证方法，如果验证有问题，主动抛出ParamError异常 并将errors作为msg参数传递过去
        valid = super(BaseForm, self).validate()
        if not valid:
            # 这里的self 就是我们常规说的验证的form
            raise ParameterException(msg=self.errors)
        return self
