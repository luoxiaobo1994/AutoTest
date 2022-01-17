# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021-07-08 12:09
import pytest


def add(a,b):
    return a+b

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
        return True

def test_add_1():
    assert add(3,4) == 7

def test_add_3():
    assert add(17,22) != 50

def test_add_4():
    print("测试大于等于")
    assert add(17,22) >= 38

if __name__ == '__main__':
    pytest.main(['-vs',"test_add_4"])