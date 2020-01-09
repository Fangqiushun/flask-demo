# -*- coding: utf-8 -*-
# @Time : 2020/1/8 22:23
# @Author : Chilson

from wtforms import IntegerField, StringField, PasswordField, widgets
from wtforms import Form
from wtforms import validators


class IntegerFieldHandler(IntegerField):
    """重写整数类型验证，将类型验证错误前置抛出"""

    def validate(self, form, extra_validators=tuple()):
        if self.process_errors:
            self.errors = list(self.process_errors)
            return len(self.errors) == 0
        else:
            return super(IntegerFieldHandler, self).validate(form, extra_validators)


class LoginForm(Form):
    username = StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空'),
            validators.length(min=6, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'placeholder': '请输入用户名'}
    )
    password = PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空'),
        ],
        render_kw={'placeholder': '请输入密码'}
    )
