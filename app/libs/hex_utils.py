"""
 Created by ldh on 18-11-22
"""
import binascii

__author__ = "ldh"


class Hex(object):

    @classmethod
    def hex_to_string(cls, hex_str):
        """
        # 16进制转字符串
        :param data:
        :return:
        """
        strs = (binascii.unhexlify(hex_str)).decode()
        print("16进制%s转字符串:%s" % (hex_str, strs))
        print("===============================")
        return strs

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
    s = "32 38 32 30 30 36 31 31 39 45 38 43 45 32 37 46 01 04 02 01 0D 79 65 64 02 01 0F FF 40 10 03 10 80 00 80 00 80 00 01 0B 80 00 80 00 80 00 01 08 E3 3B"
    s = s.split(' ')
    res = []
    for i in s:
        print(i)
        r = Hex.hex_to_string(i)
        res.append(r)
    print(''.join(res))