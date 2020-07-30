"""
 Created by ldh on 18-11-22
"""
from flask import Flask
from flask_login import LoginManager
from app.models.base import db
from flask_mail import Mail

__author__ = "ldh"

login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')  # 载入配置文件config.py
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    mail.init_app(app)

    # db.create_all(app=app)
    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web, url_prefix='/equipment')
    from app.api import api
    app.register_blueprint(api)
