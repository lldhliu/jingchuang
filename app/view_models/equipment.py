"""
 Created by ldh on 18-11-29
"""
from app.libs.enums import EquipmentType

__author__ = "ldh"


# 代码重构
class EquipmentViewModel(object):
    def __init__(self, equipment):
        self.id = equipment.id
        self.no = equipment.no
        self.cm_no = equipment.cm_no
        self.name = equipment.name
        self.producer = equipment.producer
        self.phone = equipment.phone
        self.address = equipment.address
        self.type = EquipmentType.type_str(equipment.type, 'desc')
        # self.type = equipment.type
        self.latitude = equipment.latitude
        self.longitude = equipment.longitude
        # self.data_time = self.last_data['last_time']
        # self.temperature = self.last_data['temperature']
        # self.open_count = self.last_data['open_count']
        self.mm_temp_01 = equipment.mm_temp_01
        self.mm_temp_02 = equipment.mm_temp_02
        self.mm_temp_03 = equipment.mm_temp_03
        self.mm_temp_04 = equipment.mm_temp_04
        self.fm_temp_01 = equipment.fm_temp_01
        self.fm_temp_02 = equipment.fm_temp_02
        self.fm_temp_03 = equipment.fm_temp_03
        self.fm_temp_04 = equipment.fm_temp_04
        self.open_count = equipment.open_count
        self.humidity = equipment.humidity

    # @property
    # def last_data(self):
    #     data = EquipmentData.get_last_data(self.id)
    #     if data:
    #         return dict(
    #             last_time=data.create_datetime,
    #             temperature=data.temperature,
    #             open_count=data.open_count
    #         )
    #     else:
    #         return dict(
    #             last_time=None,
    #             temperature=0,
    #             open_count=0
    #         )


class EquipmentCollection:
    def __init__(self, equipments):
        self.page = equipments.page
        self.has_prev = equipments.has_prev
        self.prev_num = equipments.prev_num
        self.next_num = equipments.next_num
        self.total = equipments.total
        self.iter_pages = equipments.iter_pages
        self.items = self.fill(equipments)

    def fill(self, equipments):
        res = [EquipmentViewModel(equipment) for equipment in equipments.items]
        # self.total = len(self.equipments)
        return res
