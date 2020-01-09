# -*- coding: utf-8 -*-
# @Time : 2019/12/22 17:03
# @Author : Chilson

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run('0.0.0.0', 80)


"""
第一阶段：请求到来
    将request和session相关数据封装导ctx=RequestContext对象中。
    再通过LocalStack将ctx添加到Local中。
    __storage__ = {
        2123:{'stack': [ctx(request, session)]}
    }
第二阶段：视图函数中获取request或session
    方式一：直接LocalStack获取
"""