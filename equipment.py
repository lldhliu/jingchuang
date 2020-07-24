# *_*coding: utf-8*_*
from app import create_app

__author__ = 'ldh'

app = create_app()


if __name__ == '__main__':
    # 生产环境 nginx+uwsgi
    # print('id为', id(app), '启动')
    app.run(host='0.0.0.0', port=5500, debug=app.config['DEBUG'])
    # 单进程, 单线程
    # 开启flask多线程  threaded=True
