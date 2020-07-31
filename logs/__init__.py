"""
 Created by 刘大怪 on 20-7-30
"""
__author__ = "刘大怪"

import os
import time


# 用log函数把所有输出写入到文件
def log(*args, **kwargs):
    t = "%Y/%m/%d %H:%M:%S"
    value = time.localtime(int(time.time()))
    # print(value)
    dt = time.strftime(t, value)
    # print(dt)
    filename = 'main_log.txt'
    path = os.path.join('logs', filename)
    with open(path, 'a', encoding='utf-8') as f:
        # 通过file参数可以把输出写入到文件f中
        print(dt, *args, file=f, **kwargs)


# 用log函数把所有输出写入到文件
def log_equ(*args, **kwargs):
    t = "%Y/%m/%d %H:%M:%S"
    value = time.localtime(int(time.time()))
    # print(value)
    dt = time.strftime(t, value)
    # print(dt)
    filename = 'equ_log.txt'
    path = os.path.join('logs', filename)
    with open(path, 'a', encoding='utf-8') as f:
        # 通过file参数可以把输出写入到文件f中
        print(dt, *args, file=f, **kwargs)
