"""
 Created by 刘大怪 on 20-6-23
"""
from flask import current_app
from sqlalchemy import Column, Integer, ForeignKey, String, SmallInteger, Float
from sqlalchemy.orm import relationship

from app.libs.enums import EquipmentType
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
    _type = Column('type', SmallInteger, comment="设备类型")
    latitude = Column(Float, comment="地理位置纬度")
    longitude = Column(Float, comment="地理位置经度")
    mm_temp_01 = Column(Float, comment='动模1温度')
    mm_temp_02 = Column(Float, comment='动模2温度')
    mm_temp_03 = Column(Float, comment='动模3温度')
    mm_temp_04 = Column(Float, comment='动模4温度')
    fm_temp_01 = Column(Float, comment='定模1温度')
    fm_temp_02 = Column(Float, comment='定模2温度')
    fm_temp_03 = Column(Float, comment='定模3温度')
    fm_temp_04 = Column(Float, comment='定模4温度')
    open_count = Column(Integer, comment='设备开合次数')
    humidity = Column(Float, comment='设备湿度')

    @property
    def type(self):  # 转化成枚举
        return EquipmentType(self._type)

    @type.setter
    def type(self, status):
        self._type = status.value

    @classmethod
    def get_equ_list(cls, page, is_admin, uid, filter_by=None, filter_content=None):
        filter = {}
        if is_admin:
            if filter_content:
                if filter_by == 'type':
                    filter['_type'] = EquipmentType.str2enum(filter_content).value
                else:
                    filter[filter_by] = filter_content
            # print(filter)
            return Equipment.query.filter_by(**filter).paginate(page, per_page=10)
        else:
            filter["uid"] = uid
            if filter_content:
                if filter_by == 'type':
                    filter['_type'] = EquipmentType.str2enum(filter_content).value
                else:
                    filter[filter_by] = filter_content
            return Equipment.query.filter_by(**filter).paginate(page, per_page=10)

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']

    @classmethod
    def get_equ_ids(cls, uid):
        equipments = Equipment.query.filter_by(uid=uid).all()
        return [e.id for e in equipments] if equipments else []
