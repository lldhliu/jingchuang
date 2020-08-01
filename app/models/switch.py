"""
 Created by 刘大怪 on 20-6-23
"""
from sqlalchemy import Column, Integer, ForeignKey, String, SmallInteger, desc
from sqlalchemy.orm import relationship

from app.libs.enums import EquipmentType
from app.models.base import Base
from app.models.equipment import Equipment

__author__ = "ldh"


# 设备开合数据记录表
class Switch(Base):
    id = Column(Integer, primary_key=True)
    equipment = relationship('Equipment')
    equ_id = Column(Integer, ForeignKey('equipment.id'))  # 外键
    switch = Column(SmallInteger, comment='开合状态')
    count = Column(Integer, comment='设备开合次数统计')
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
            # r = Switch.query.join(Equipment, Equipment.id==Switch.equ_id).filter_by(**filter)\
            #     .paginate(page, per_page=10)
            return Switch.query.join(Equipment, Equipment.id==Switch.equ_id).filter_by(**filter)\
                .paginate(page, per_page=10)

        else:
            filter['uid'] = uid
            if filter_content:
                if filter_by == "type":
                    filter['_type'] = EquipmentType.str2int(filter_content).value
                else:
                    filter[filter_by] = filter_content
            return Switch.query.join(Equipment, Equipment.id==Switch.equ_id).filter_by(**filter)\
                .paginate(page, per_page=10)

    @classmethod
    def get_last_data(cls, equ_id):
        return Switch.query.filter_by(equ_id=equ_id).order_by(desc(Switch.create_time)).first()

    @property
    def equ_summary(self):
        return Equipment.query.filter_by(id=self.equ_id).first()
