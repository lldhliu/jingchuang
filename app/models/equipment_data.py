"""
 Created by 刘大怪 on 20-6-23
"""
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, SmallInteger, Float
from sqlalchemy.orm import relationship

from app.models.base import Base

__author__ = "ldh"


# 设备数据记录表
class EquipmentData(Base):
    id = Column(Integer, primary_key=True)

    equipment = relationship('Equipment')
    equ_id = Column(Integer, ForeignKey('equipment.id'))  # 外键

    temperature = Column(Float, comment='温度')
    open_count = Column(Integer, comment='合模次数')

    @classmethod
    def get_data_list(cls, page, equ_ids=None):
        if equ_ids is None:
            # a = EquipmentData.query.paginate(page, per_page=10)
            return EquipmentData.query.paginate(page, per_page=10)
        b = EquipmentData.query.filter(EquipmentData.equ_id.in_(equ_ids)).paginate(page, per_page=10)
        return EquipmentData.query.filter(EquipmentData.equ_id.in_(equ_ids)).paginate(page, per_page=10)

