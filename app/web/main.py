from flask import render_template
from flask_login import login_required, current_user
from app.models.user import User
from app.web import web

__author__ = '七月'


@web.route('/')
def index():
    # recent_gifts = Gift.recent()
    books = []

    return render_template('index.html', recent=books)


@web.route('/personal')
@login_required
def personal_center():
    user = User.query.filter_by(id=current_user.id).first()
    if user:
        auth = user.summary
        return render_template('personal.html', user=auth)
