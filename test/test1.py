"""
 Created by ldh on 18-11-29
"""
from flask import Request

__author__ = "ldh"

import threading
import time


def worker():
    print('i am thread')
    t = threading.current_thread()
    time.sleep(10)
    print(t.getName())


new_t = threading.Thread(target=worker, name='ldh_thread')
new_t.start()


print(' ni hao')
t = threading.current_thread()  # 主线程
print(t.getName())



