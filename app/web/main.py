from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models.user import User, get_user_list
from app.web import web

__author__ = '七月'


@web.route('/')
@web.route('/<int:page>')
@login_required
def index(page=1):
    if current_user.nickname == "admin":
        users = get_user_list(page)
        return render_template('index.html', users=users)
    return redirect(url_for("web.equipment"))


@web.route('/personal')
@login_required
def personal_center():
    user = User.query.filter_by(id=current_user.id).first()
    if user:
        auth = user.summary
        return render_template('personal.html', user=auth)
