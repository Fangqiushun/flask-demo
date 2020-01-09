# -*- coding: utf-8 -*-
# @Time : 2019/12/15 17:27
# @Author : Chilson
from DBUtils.PooledDB import PooledDB
import pymysql


class BaseConfig:
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True
    SALT = b'f#$jlk!'       # md5盐值
    SECRET_KEY = 'lkh@#%'   # session加密key值
    # 数据库连接池
    POOL = PooledDB(
        creator=pymysql,    # 使用连接数据库的模块
        maxconnections=6,   # 连接池允许的最大连接数，0和None表示不限制连接数
        mincached=2,        # 初始化时，连接池中至少创建的空闲连接数
        maxcached=5,        # 连接池中最多限制的链接数
        blocking=True,      # 连接池中如果没有可用的连接后，是否阻塞等待
        maxusage=None,      # 一个连接最多被重复使用的次数，None表示无限制
        setsession=[],      # 开始会话前执行的命令列表
        ping=0,             # ping MySQL服务器，0=None=Never
        host='127.0.0.1',
        port=3306,
        user='root',
        password='12345678',
        database='demo',
        charset='utf8'
    )


class ProductionConfig(BaseConfig):
    pass

Config = DevelopmentConfig