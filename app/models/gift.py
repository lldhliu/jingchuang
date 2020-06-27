"""
 Created by ldh on 18-12-3
"""
from flask import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, SmallInteger, desc, func
from sqlalchemy.orm import relationship
from app.models.base import Base, db
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from collections import namedtuple

__author__ = "ldh"

EachGiftWishCount = namedtuple('EachGiftWishCount', ['count', 'isbn'])


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))  # 外键
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))  # 外键
    launched = Column(Boolean, default=False)

    def is_yourself_gift(self, uid):
        return True if self.uid == uid else False

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        # 根据传入的一组isbn, 到Gift表中检索出相应的礼物,
        # 并且计算出某个礼物的Wish心愿数量
        # filter接收条件表达式
        # mysql in查询
        isbn_list = isbn_list
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1).group_by(
            Wish.isbn).all()
        # count_list = [EachGiftWishCount(w[0], w[1]) for w in count_list]

        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # 对象代表一个礼物, 具体
    # 类代表礼物这个事物, 它是抽象, 不是具体的"一个"
    @classmethod
    def recent(cls):
        # 链式调用
        # 主体 Query
        # 子函数 oredr_by  group_by...
        # 触发语句 all() first()
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        # print(recent_gift)
        return recent_gift
