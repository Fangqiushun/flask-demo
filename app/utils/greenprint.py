# -*- coding: utf-8 -*-
# @Time : 2019/12/22 16:02
# @Author : Chilson
import copy


class Greenprint:
    """绿图：在蓝图之前做动作，添加一层url配置
    用法（生成v1版本的用户认证方面的登录接口：/v1/auth/login）：
        api = Greenprint('auth')
        @api.route('/login')
        def route():
            return 'login'
        bp_v1 = Blueprint('v1', __name__)
        new_bp_v1 = api.register(bp_v1)
    """

    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f

        return decorator

    def register(self, bp, url_prefix=None):
        """
        注册蓝本，生成新的蓝本
        :param bp: 蓝本
        :param url_prefix: url前缀
        :return:
        """
        self.bp = copy.deepcopy(bp)

        # 蓝图名称拼接绿图名称，使url和url_for参数对应方式统一（/v1/auth/login 对应 v1.auth.login）
        self.bp.name += '.' + self.name

        if url_prefix is None:
            url_prefix = '/' + self.name

        for f, rule, options in self.mound:
            endpoint = options.pop("endpoint", f.__name__)
            self.bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
        return self.bp
