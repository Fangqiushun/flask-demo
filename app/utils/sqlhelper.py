# -*- coding: utf-8 -*-
# @Time : 2020/1/5 19:19
# @Author : Chilson

import pymysql
from app.config import Config


def connect():
    """
    创建数据库连接
    :return:
    """
    conn = Config.POOL.connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor


def close(conn, cursor):
    """
    关闭数据库连接
    :param conn: 数据库连接
    :param cursor: 数据库游标
    :return:
    """
    conn.close()
    cursor.close()


def fetch_one(sql, args):
    """
    单条记录查询
    :param sql: sql语句
    :param args: sql需要拼接的参数
    :return:
    """
    conn, cursor = connect()
    cursor.execute(sql, args)
    data = cursor.fetchone()
    close(conn, cursor)
    return data


def fetch_all(sql, args):
    """
    多条记录查询
    :param sql: sql语句
    :param args: sql需要拼接的参数
    :return:
    """
    conn, cursor = connect()
    cursor.execute(sql, args)
    data = cursor.fetchone()
    close(conn, cursor)
    return data


def insert(sql, args):
    conn, cursor = connect()
    row = cursor.execute(sql, args)
    close(conn, cursor)
    return row
