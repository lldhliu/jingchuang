"""
 Created by ldh on 18-11-22
"""
import binascii

__author__ = "ldh"

import requests


class HTTP(object):
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful
        # json格式
        # 以下是简化写法
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

        # 以下是普通写法，不建议
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''


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
    Hex.hex_to_string("e6b58be8af95e5ad97e7aca6e4b8b2")
