"""
 Created by 刘大怪 on 20-6-23
"""
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, SmallInteger, Float
from sqlalchemy.orm import relationship

from app.models.base import Base

__author__ = "ldh"


class Equipment(Base):
    id = Column(Integer, primary_key=True)

    # user = relationship('User')
    # uid = Column(Integer, ForeignKey('user.id'))  # 外键

    no = Column(String(100), nullable=False, unique=True, index=True, comment="设备编号")
    name = Column(String(50), nullable=False, index=True, comment="设备名称")
    producer = Column(String(100), comment="制造商")
    phone = Column(String(18), comment="联系电话")
    address = Column(String(200), comment="设备地址")
    type = Column(SmallInteger, comment="设备类型")
    latitude = Column(Float, comment="地理位置纬度")
    longitude = Column(Float, comment="地理位置经度")
