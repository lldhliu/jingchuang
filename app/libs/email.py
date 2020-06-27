"""
 Created by ldh on 18-12-5
"""
from flask import current_app, render_template
from threading import Thread
from app import mail
from flask_mail import Message

__author__ = "ldh"


# 异步发送邮件
def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            raise e


def send_mail(to, subject, template, **kwargs):
    """
    :param to: 用户邮箱地址
    :param subject: 邮件标题
    :param template: 模板名称
    :param kwargs: 模板里面参数
    :return:
    """
    # Python flask email库 pip install flask-mail
    # msg = Message('测试邮件', sender='1151375085@qq.com', body='Test',
    #               recipients=['ldh1151375085@163.com'])
    msg = Message('[鱼书]'+' '+subject, sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
