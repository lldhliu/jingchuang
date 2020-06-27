"""
 Created by ldh on 18-11-22
"""
from flask import Blueprint, render_template

__author__ = "ldh"

# 蓝图 blueprint 蓝本
api = Blueprint('api', __name__)


@api.app_errorhandler(404)
def not_found(e):
    # AOP 思想 ==> 面向切片编程
    # 通用异常处理逻辑都可以放在这里
    return render_template('404.html'), 404


# from app.api import book
# from app.api import auth
# from app.web import drift
# from app.web import gift
# from app.web import main
# from app.web import wish
from app.api import book1
# from app.web import user
