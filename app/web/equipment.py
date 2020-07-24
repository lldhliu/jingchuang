"""
 Created by ldh on 18-11-22
"""
from flask import request, render_template, redirect, url_for
from flask_login import current_user

from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel
from app.view_models.trade import TradeInfo
from . import web

__author__ = "ldh"

# # 第二种注册路由方式（使用基于类的视图（即插视图）方式使用）
# app.add_url_rule('/hello', view_func=hello)


@web.route('/equipment', methods=['POST', 'GET'])  # 第一种注册路由方式（一般使用）
def equipment():

    equipments = []
    return render_template('equipment.html', equipments=equipments)


@web.route('/equipment/create', methods=['POST', 'GET'])
def equipment_create():
    if request.method == 'POST':
        return redirect(url_for('web.equipment'))
    return render_template('equipment_create.html')


@web.route('/equipment/data', methods=['POST', 'GET'])
def equipment_data():
    if request.method == 'POST':
        return redirect(url_for('web.equipment_data'))
    return render_template('equipment_data.html')


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    # 取书籍详细数据
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template('book_detail.html', book=book,
                           wishes=trade_wishes_model, gifts=trade_gifts_model,
                           has_in_wishes=has_in_wishes, has_in_gifts=has_in_gifts)
