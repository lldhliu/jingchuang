"""
 Created by ldh on 18-11-29
"""
__author__ = "ldh"


# 代码重构
class EquipmentViewModel:
    def __init__(self, equipment, equdata):
        self.no = equipment['no']
        self.name = equipment['name']
        self.producer = equipment['producer']
        self.phone = equipment['phone']
        self.address = equipment['address']
        self.type = equipment['type']
        self.temperature = equdata['temperature']
        self.open_count = equdata['open_count']
        self.data_time = equdata['create_datetime']


class EquipmentCollection:
    def __init__(self):
        self.total = 0
        self.equipments = []

    def fill(self, equipments, equdatas):
        self.equipments = [EquipmentViewModel(equipment, equdata) for equipment, equdata in zip(equipments, equdatas)]
        self.total = len(self.equipments)
