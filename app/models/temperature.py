"""
 Created by 刘大怪 on 20-6-23
"""
from sqlalchemy import Column, Integer, ForeignKey, String, Float, desc
from sqlalchemy.orm import relationship

from app.libs.enums import EquipmentType
from app.models.base import Base
from app.models.equipment import Equipment

__author__ = "ldh"


# 设备温度记录表
class Temperature(Base):
    id = Column(Integer, primary_key=True)
    equipment = relationship('Equipment')
    equ_id = Column(Integer, ForeignKey('equipment.id'))  # 外键
    mm_temp_01 = Column(Float, comment='动模1温度')
    mm_temp_02 = Column(Float, comment='动模2温度')
    mm_temp_03 = Column(Float, comment='动模3温度')
    mm_temp_04 = Column(Float, comment='动模4温度')
    fm_temp_01 = Column(Float, comment='定模1温度')
    fm_temp_02 = Column(Float, comment='定模2温度')
    fm_temp_03 = Column(Float, comment='定模3温度')
    fm_temp_04 = Column(Float, comment='定模4温度')
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
            # r = Temperature.query.join(Equipment, Equipment.id==Temperature.equ_id).filter_by(**filter)\
            #     .paginate(page, per_page=10)
            return Temperature.query.join(Equipment, Equipment.id==Temperature.equ_id).filter_by(**filter)\
                .paginate(page, per_page=10)

        else:
            filter['uid'] = uid
            if filter_content:
                if filter_by == "type":
                    filter['_type'] = EquipmentType.str2int(filter_content).value
                else:
                    filter[filter_by] = filter_content
            return Temperature.query.join(Equipment, Equipment.id==Temperature.equ_id).filter_by(**filter)\
                .paginate(page, per_page=10)

    @classmethod
    def get_last_data(cls, equ_id):
        return Temperature.query.filter_by(equ_id=equ_id).order_by(desc(Temperature.create_time)).first()

    @property
    def equ_summary(self):
        return Equipment.query.filter_by(id=self.equ_id).first()
