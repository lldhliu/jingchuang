"""
 Created by ldh on 18-11-22
"""
from app.libs.httper import HTTP
from flask import current_app

__author__ = "ldh"


class YuShuBook:
    # def __init__(self):
    #     self.isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    #     self.keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = YuShuBook.isbn_url.format(isbn)
        # url = self.isbn_url
        result = HTTP.get(url)
        # 需要用到数据库的伪代码
        # book = query_from_mysql(isbn)
        # if book:
        #     return book
        # else:
        #     save(book)
        self.__fill_single(result)

    def __fill_single(self, data):
        # 处理单本数据
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        # 处理关键字查询数据
        self.total = data['total']
        self.books = data['books']

    def search_by_keyword(self, keyword, page=1):
        url = YuShuBook.keyword_url.format(keyword, current_app.config['PER_PAGE'],
                                           self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def calculate_start(self, page):
        return (page-1)*current_app.config['PER_PAGE']

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None
