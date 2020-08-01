"""
 Created by ldh on 18-11-29
"""
from app.libs.enums import EquipmentType

__author__ = "ldh"


# 代码重构
class HumidityModel(object):
    def __init__(self, humidity):
        self.id = humidity.id
        self.equ_id = humidity.equ_id
        self.humidity = humidity.humidity
        self.create_datetime = humidity.create_datetime
        self.equ_name = humidity.equ_summary.name
        self.equ_no = humidity.equ_summary.no
        self.equ_type = EquipmentType.type_str(humidity.equ_summary.type, 'desc')
        # self.equ_type = data.equ_summary.type
        self.raw_data = humidity.raw_data


class HumidityCollection:
    def __init__(self, humidities):
        self.page = humidities.page
        self.has_prev = humidities.has_prev
        self.prev_num = humidities.prev_num
        self.next_num = humidities.next_num
        self.total = humidities.total
        self.iter_pages = humidities.iter_pages
        self.items = self.fill(humidities)

    def fill(self, switchs):
        res = [HumidityModel(data) for data in switchs.items]
        # self.total = len(self.equipments)
        return res
