"""
 Created by 刘大怪 on 20-7-30
"""
import binascii

__author__ = "刘大怪"


class Hex(object):
    @classmethod
    def hex_to_string(cls, hex_str):
        """
        # 16进制转字符串
        :param hex_str:
        :return:
        """
        str = (binascii.unhexlify(hex_str)).decode()
        # print("16进制%s转字符串:%s" % (hex_str, str))
        return str

    @classmethod
    def split_temp_data(cls, hex_str):
        # todo
        pass

    @classmethod
    def string_to_hex(cls, str):
        """
        # 字符串转16进制
        :param str:
        :return:
        """
        hex_str = binascii.b2a_hex(str.encode('utf-8'))
        # print("字符串%s转16进制:%s" % (str, hex_str))
        return hex_str


if __name__ == "__main__":
    Hex.hex_to_string("e6b58be8af95e5ad97e7aca6e4b8b2")
    Hex.string_to_hex("测试字符串")
