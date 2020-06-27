"""
 Created by ldh on 18-11-29
"""
import time

__author__ = "ldh"


# LocalStack线程隔离特性
from werkzeug.local import LocalStack
import threading

my_stack = LocalStack()
my_stack.push(1)
print("in main thread after push, value is: ", my_stack.top)


def worker():
    # 新线程
    print('in new thread before push, value is: ', my_stack.top)
    my_stack.push(2)
    # my_stack.push(3)
    print('in new thread after push, value is: ', my_stack.top)


new_t = threading.Thread(target=worker, name='devin_thread')
new_t.start()
time.sleep(1)
# 主线程
print('finally, in main thread value is: ', my_stack.top)
