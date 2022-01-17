# -*- coding:utf-8 -*-
# Author:Luoxiaobo
# Time: 2021/6/30 22:31

import unittest
from ddt import ddt,data,unpack
import random

@ddt
class First(unittest.TestCase):

    def test_001(self):
        """ 测试加法 """
        a = 1
        b = 2
        self.assertEqual(a+b,3)

    def test_002(self):
        """ 测试减法 """
        a = 1
        b = 2
        self.assertEqual(a-b,5)

    @data([1,2],[3,4],[5,6],[5,5],[7,8])
    @unpack
    def test_003(self,a,b):
        """ 测试ddt传参 """
        self.assertEqual(a+b,a+b+random.choice([0,0,0,0,1]))
