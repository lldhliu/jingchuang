"""
 Created by ldh on 18-12-6
"""
__author__ = "ldh"
from enum import Enum


class EquipmentType(Enum):
    """
    设备类型
    """
    hardware_mold = 1
    plastic_mold = 2

    @classmethod
    def type_str(cls, status, key):
        key_map = {
            cls.hardware_mold: {
                'desc': '五金模具',
            },
            cls.plastic_mold: {
                'desc': '注塑模具',
            }
        }
        return key_map[status][key]

    # 根据类型描述生成枚举类型
    @classmethod
    def str2enum(cls, str):
        key_map = {
            '五金模具': cls.hardware_mold,
            '注塑模具': cls.plastic_mold
        }
        return key_map[str]


class QueryType(Enum):
    """
    查询条件
    """
    # 设备编号
    no = 1
    # 设备名称
    name = 2
    # 设备类型
    type = 3


class DataType(Enum):
    """
    数据类型
    """
    # 温度
    temperature = 1
    # 开关状态
    switch = 2
    # 湿度
    humidity = 3


if __name__ == '__main__':
    print(DataType['temperature'])
