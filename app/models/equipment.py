"""
 Created by 刘大怪 on 20-6-23
"""
from flask import current_app
from sqlalchemy import Column, Integer, ForeignKey, String, SmallInteger, Float
from sqlalchemy.orm import relationship

from app.models.base import Base

__author__ = "ldh"


class Equipment(Base):
    id = Column(Integer, primary_key=True)

    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))  # 外键

    no = Column(String(100), nullable=False, unique=True, index=True, comment="设备编号")
    cm_no = Column(String(100), nullable=False, unique=True, index=True, comment="4g通信模块编号")
    name = Column(String(50), nullable=False, index=True, comment="设备名称")
    producer = Column(String(100), comment="制造商")
    phone = Column(String(18), comment="联系电话")
    address = Column(String(200), comment="设备地址")
    type = Column(SmallInteger, comment="设备类型")
    latitude = Column(Float, comment="地理位置纬度")
    longitude = Column(Float, comment="地理位置经度")

    @classmethod
    def get_equ_list(cls, page, uid=-1):
        if uid == -1:
            return Equipment.query.paginate(page, per_page=10)
        return Equipment.query.filter_by(uid=uid).paginate(page, per_page=10)

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']

    @classmethod
    def get_equ_ids(cls, uid):
        equipments = Equipment.query.filter_by(uid=uid).all()
        return [e.id for e in equipments] if equipments else []