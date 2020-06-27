"""
 Created by ldh on 18-11-23
"""
__author__ = "ldh"

from flask import Flask, current_app


app = Flask(__name__)
# # 应用上下文 对象 Flask
# # 请求上下文 对象 Request
# # Flask AppContext
# # Request RequestContext
# # 离线应用、单元测试
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

# with
# with app.app_context():  # 上下文表达式（必须返回上下文管理器）
#     a = current_app
#     d = current_app.config['DEBUG']

# with 使用场景
# 实现了上下文协议的对象
# 上下文管理器
# __enter__  __exit__


class MyResource:
    # def __enter__(self):
    #     print('connect to resource')
    #     return self
    #
    # def __exit__(self, exc_type, exc_value, tb):
    #     if tb:
    #         print('process exception')
    #     else:
    #         print('no execption')
    #     print('close resource connetion')
    #     return False  # 返回True, with语句外部不会再抛出异常   返回False, with语句外部会再次抛出异常  什么都不返回默认十None,也就是False

    def query(self):
        print('query data')


try:
    with MyResource() as resource:
        # 1/0
        resource.query()
except Exception as ex:
    pass


from contextlib import contextmanager


@contextmanager   # 把不是上下文管理器的类转化为上下文管理器对象
def make_myresource():
    print('connect to resource')
    yield MyResource()
    print('close resource connetion')


# yield 生成器
with make_myresource() as resource:
    resource.query()
