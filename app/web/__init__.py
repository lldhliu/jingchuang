"""
 Created by ldh on 18-11-22
"""
from flask import Blueprint, render_template

__author__ = "ldh"

# 蓝图 blueprint 蓝本
web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def not_found(e):
    # AOP 思想 ==> 面向切片编程
    # 通用异常处理逻辑都可以放在这里
    return render_template('404.html'), 404


from app.web import auth
from app.web import main
from app.web import equipment
