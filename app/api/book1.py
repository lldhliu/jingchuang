"""
 Created by ldh on 18-11-22
"""
from flask import jsonify, request, flash, render_template
from flask_login import current_user

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection
from app.view_models.trade import TradeInfo
from app.web import web
from app.api import api
import json


__author__ = "ldh"

# # 第二种注册路由方式（使用基于类的视图（即插视图）方式使用）
# app.add_url_rule('/hello', view_func=hello)


@api.route('/api/book/search')  # 第一种注册路由方式（一般使用）
def search():
    """
        q:普通关键字 isbn
        page:
        ?q=xx&page=1
    """
    # # 将不可变字典转为可变字典 a=request.args.to_dict()
    # q = request.args['q']
    # # q至少一个字符，长度限制
    # page = request.args['page']
    # # page正整数， 也要有一个最大值限制

    '''验证层'''
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)  # 导入快捷键alt+enter
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books)  # 序列化无法直接操作对象
        # return json.dumps(result), 200, {'content-type': 'application/json'}
    else:
        flash('搜索的关键字不符合要求, 请重新输入关键字')
        return jsonify(form.errors)
    # return render_template('search_result.html', books=books)
