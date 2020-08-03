"""
 Created by ldh on 18-11-29
"""
from app.libs.enums import EquipmentType

__author__ = "ldh"


# 代码重构
class TemperatureViewModel(object):
    def __init__(self, temperature):
        self.id = temperature.id
        self.equ_id = temperature.equ_id
        self.mm_temp_01 = temperature.mm_temp_01
        self.mm_temp_02 = temperature.mm_temp_02
        self.mm_temp_03 = temperature.mm_temp_03
        self.mm_temp_04 = temperature.mm_temp_04
        self.fm_temp_01 = temperature.fm_temp_01
        self.fm_temp_02 = temperature.fm_temp_02
        self.fm_temp_03 = temperature.fm_temp_03
        self.fm_temp_04 = temperature.fm_temp_04
        self.create_datetime = temperature.create_datetime
        self.equ_name = temperature.equ_summary.name
        self.equ_no = temperature.equ_summary.no
        self.equ_type = EquipmentType.type_str(temperature.equ_summary.type, 'desc')
        # self.equ_type = data.equ_summary.type
        self.raw_data = temperature.raw_data


class TemperatureCollection:
    def __init__(self, temperatures):
        self.page = temperatures.page
        self.has_prev = temperatures.has_prev
        self.prev_num = temperatures.prev_num
        self.next_num = temperatures.next_num
        self.has_next = temperatures.has_next
        self.total = temperatures.total
        self.iter_pages = temperatures.iter_pages
        self.items = self.fill(temperatures)

    def fill(self, temperatures):
        res = [TemperatureViewModel(data) for data in temperatures.items]
        # self.total = len(self.equipments)
        return res
