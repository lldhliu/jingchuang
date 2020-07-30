"""
 Created by ldh on 18-12-3
"""
from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, SmallInteger, Integer, String

__author__ = "ldh"


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'del_flag' not in kwargs.keys():
            kwargs['del_flag'] = 0
        return super(Query, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)


# 基类模型
class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    create_by = Column(String(24))
    update_time = Column('update_time', Integer)
    update_by = Column(String(24))
    status = Column(SmallInteger, default=1)
    del_flag = Column(SmallInteger, default=0)

    def __init__(self):
        if self.is_update():
            self.update_time = int(datetime.now().timestamp())
        else:
            self.create_time = int(datetime.now().timestamp())
            self.update_time = int(datetime.now().timestamp())

    def is_update(self):
        if self.create_time:
            return True
        return False

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    @property
    def update_datetime(self):
        if self.update_time:
            return datetime.fromtimestamp(self.update_time)
        else:
            return None

    def delete(self):
        self.del_flag = 1
