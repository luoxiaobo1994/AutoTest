# -*- coding:utf-8 -*-
# Author:Luoxiaobo
# Time: 2021/7/6 23:09
import re
import time,random
from base.common import runtime

@runtime
def foo():
    sum = 0
    for i in range(10000000):
        sum += i
    print(sum)



def get_arg(func):
    def inner(*args):
        func(*args)
        print(*args)
    return inner

@get_arg
def a(a,b):
    print(a+b)

