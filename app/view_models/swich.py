"""
 Created by ldh on 18-11-29
"""
from app.libs.enums import EquipmentType

__author__ = "ldh"


# 代码重构
class SwichViewModel(object):
    def __init__(self, swich):
        self.id = swich.id
        self.equ_id = swich.equ_id
        self.swich = swich.swich
        self.count = swich.count
        self.create_datetime = swich.create_datetime
        self.equ_name = swich.equ_summary.name
        self.equ_no = swich.equ_summary.no
        self.equ_type = EquipmentType.type_str(swich.equ_summary.type, 'desc')
        # self.equ_type = data.equ_summary.type


class SwichCollection:
    def __init__(self, swichs):
        self.page = swichs.page
        self.has_prev = swichs.has_prev
        self.prev_num = swichs.prev_num
        self.next_num = swichs.next_num
        self.total = swichs.total
        self.iter_pages = swichs.iter_pages
        self.items = self.fill(swichs)

    def fill(self, swichs):
        res = [SwichViewModel(data) for data in swichs.items]
        # self.total = len(self.equipments)
        return res
