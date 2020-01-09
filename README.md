# flask_demo
flask应用通用脚手架

## 目录结构
```
|-- app                         
|   |-- api                     # api入口
|   |   -- v1
|   |       |-- auth.py
|   |       |-- __init__.py
|   |-- config.py               # 配置文件
|   |-- decorators.py           # 装饰器
|   |-- forms.py                # 表单验证类
|   |-- __init__.py
|   |-- static                  # 静态文件
|   |   |-- 1.jpg
|   |   |-- 2.jpg
|   |   |-- 3.jpg
|   |   |-- 4.jpg
|   |   |-- 5.jpg
|   |   |-- 6.jpg
|   |-- templates               # 静态页面
|   |   |-- index.html
|   |   |-- login.html
|   |-- utils                   # 工具类
|   |   |-- greenprint.py       # 绿图
|   |   |-- md5.py              # md5加密
|   |   |-- sqlhelper.py        # sql操作基本类
|   |-- views                   # 页面路由
|       |-- auth.py
|       |-- index.py
|       |-- __init__.py
|-- app.py                      # 应用启动入口
|-- README.md
|-- requirements.txt            # 依赖
|-- uwsgi.ini                   # 部署需要的配置文件            
```

