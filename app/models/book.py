"""
 Created by ldh on 18-11-22
"""
from sqlalchemy import Column, Integer, String

from app.models.base import db

__author__ = "ldh"


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))  # 精装 平装
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))  # 出版日期
    isbn = Column(String(15), nullable=False, unique=True)  # 独一无二不重复unique=True
    summary = Column(String(1000))  # 简介
    image = Column(String(50))

    def sample(self):
        pass