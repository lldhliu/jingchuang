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

    @classmethod
    def byte16ToInt(cls, byte16):
        byte16 = hex(byte16)
        if ((byte16 & 0x8000) == 0):
            r = byte16
        else:
            byte16 = byte16 ^ 0xffff
            byte16 = byte16 + 1
            r = - byte16
        return r

    @classmethod
    # 求反码
    def Getadverse(cls, trueform):
        ad = list(trueform)
        # a = ""
        for i in range(len(ad)):
            if ad[i] == '0':
                ad[i] = '1'
            else:
                ad[i] = '0'
        a = "".join(ad)
        return a


if __name__ == "__main__":
    S = {'cmid': '282006119E8CE27F', 'data': '10031080008000800001348000800080000133B71922556402010E3E80225510031080008000800001348000800080000133B719'}

    c = S['data']
    l = c.split("2255")
    # print(l)
    temp = l[0][6: 38]
    # print(temp)
    for i in range(8):
        bin_i = temp[i*4: i*4+4]
        a = bin(int(bin_i, 16)).replace('0b', '')
        # print(int(bin_i, 16))
        if bin_i == '8000':
            print(None)
        elif len(a) == 16 and a[0] == '1':
            # print(Hex.Getadverse(a))
            a = Hex.Getadverse(a)
            print(~int(a, 2)/10)
        else:
            print(int(bin_i, 16)/10)
        #print(~int(Hex.Getadverse(a), 2))

    # r = int('8000', 16)
    # print(int('8000', 16))
    # print(bin(int('8000', 16)).replace('0b', ''))
    # aa = bin(int('8000', 16)).replace('0b', '')
    # print(int(aa, 2))
    # bb = r - 1
    # print(int(bin(~bb), 2))
    # print(bin(int('FFF8', 16)))
    # print(~int(bin(0b1111111111111000), 2))
    # print(int(bin(~int('8000', 16)+1)), 2)
    # print(~int('0000000101111110', 2))

