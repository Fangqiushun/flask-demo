# -*- coding: utf-8 -*-
# @Time : 2019/12/22 17:03
# @Author : Chilson

from app import create_app
from app.utils.errors import APIException, HTTPException
from app.utils.error_code import ServerError

app = create_app()


@app.errorhandler(Exception)
def errorHandler(e):
    if isinstance(e, APIException):
        # 已知异常
        return e
    if isinstance(e, HTTPException):
        # HTTP异常
        code = e.code
        msg = e.description
        error_code = 1005  # 自定义
        return APIException(msg, code, error_code)
    else:
        # 其他未知异常,此处需要分是生产环境还是开发环境，如果是生产环境，返回json格式的异常，如果是开发环境，我们需要详细的异常说明去分析异常原因
        if not app.config["DEBUG"]:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run('0.0.0.0', 5500)


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
