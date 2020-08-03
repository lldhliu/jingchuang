"""
 Created by 刘大怪 on 20-6-23
"""
from sqlalchemy import Column, Integer, ForeignKey, String, Float, desc
from sqlalchemy.orm import relationship

from app.libs.enums import EquipmentType
from app.models.base import Base
from app.models.equipment import Equipment
from app.setting import PER_PAGE

__author__ = "ldh"


# 设备湿度记录表
class Humidity(Base):
    id = Column(Integer, primary_key=True)
    equipment = relationship('Equipment')
    equ_id = Column(Integer, ForeignKey('equipment.id'))  # 外键
    humidity = Column(Float, comment='设备湿度')
    raw_data = Column(String(1024), comment='原始数据')

    @classmethod
    def get_data_list(cls, page, is_admin, uid, filter_by=None, filter_content=None):
        filter = {}
        if is_admin:
            if filter_content:
                if filter_by == "type":
                    filter['_type'] = EquipmentType.str2int(filter_content).value
                else:
                    filter[filter_by] = filter_content
            r = Humidity.query.join(Equipment, Equipment.id==Humidity.equ_id).filter_by(**filter)\
                .paginate(page, per_page=PER_PAGE)
            return Humidity.query.join(Equipment, Equipment.id==Humidity.equ_id).filter_by(**filter)\
                .paginate(page, per_page=PER_PAGE)

        else:
            filter['uid'] = uid
            if filter_content:
                if filter_by == "type":
                    filter['_type'] = EquipmentType.str2int(filter_content).value
                else:
                    filter[filter_by] = filter_content
            return Humidity.query.join(Equipment, Equipment.id==Humidity.equ_id).filter_by(**filter)\
                .paginate(page, per_page=PER_PAGE)

    @classmethod
    def get_last_data(cls, equ_id):
        return Humidity.query.filter_by(equ_id=equ_id).order_by(desc(Humidity.create_time)).first()

    @property
    def equ_summary(self):
        return Equipment.query.filter_by(id=self.equ_id).first()
