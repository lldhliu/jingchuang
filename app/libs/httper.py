"""
 Created by ldh on 18-11-22
"""
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
