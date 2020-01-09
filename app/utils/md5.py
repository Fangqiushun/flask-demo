# -*- coding: utf-8 -*-
# @Time : 2020/1/5 13:10
# @Author : Chilson

import hashlib
from app.config import Config


def md5(arg):
    hash = hashlib.md5(Config.SALT)
    hash.update(bytes(arg, encoding='utf-8'))
    return hash.hexdigest()


if __name__ == '__main__':
    print(md5('chilson2go'))