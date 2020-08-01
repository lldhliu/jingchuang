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
        # str = (binascii.unhexlify(hex_str))
        print("16进制%s转字符串:%s" % (hex_str, str))
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
    # s = "32383230303631313945384345323746010402010D79656402010FFF40100310800080008000010B8000800080000108E33B"
    s = "100310800080008000010B8000800080000108E33B"
    print(s[18:22])
    print(int(s[18:22], 16))
    # print(res)

