"""
 Created by ldh on 18-11-29
"""
from app.libs.enums import EquipmentType, SwitchEnum

__author__ = "ldh"


# 代码重构
class SwitchViewModel(object):
    def __init__(self, switch):
        self.id = switch.id
        self.equ_id = switch.equ_id
        self.switch = SwitchEnum.desc(switch.switch, 'desc')
        self.count = switch.count
        self.create_datetime = switch.create_datetime
        self.equ_name = switch.equ_summary.name
        self.equ_no = switch.equ_summary.no
        self.equ_type = EquipmentType.type_str(switch.equ_summary.type, 'desc')
        # self.equ_type = data.equ_summary.type
        self.raw_data = switch.raw_data


class SwitchCollection:
    def __init__(self, switchs):
        self.page = switchs.page
        self.has_prev = switchs.has_prev
        self.prev_num = switchs.prev_num
        self.next_num = switchs.next_num
        self.has_next = switchs.has_next
        self.total = switchs.total
        self.iter_pages = switchs.iter_pages
        self.items = self.fill(switchs)

    def fill(self, switchs):
        res = [SwitchViewModel(data) for data in switchs.items]
        # self.total = len(self.equipments)
        return res
