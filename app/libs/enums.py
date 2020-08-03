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


class SwitchEnum(Enum):
    """
    数据类型
    """
    open = 1
    close = 0

    @classmethod
    def desc(cls, status, key):
        key_map = {
            cls.open: {
                'desc': '打开',
            },
            cls.close: {
                'desc': '合上',
            }
        }
        return key_map[status][key]


if __name__ == '__main__':
    print(SwitchEnum.desc())
