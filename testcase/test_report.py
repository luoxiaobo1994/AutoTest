# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/6 22:53
# Desc: 测试一下allure报告
import os
from time import sleep

import pytest


class Test_Allure():

    def setup_class(self):
        sleep(1)
        print("这个类里，只执行1次的开始函数：打开浏览器。")

    def teardown_class(self):
        sleep(1)
        print("这个类里，只执行1次的扫尾函数：关闭浏览器。")
        os.system(r"allure generate D:\AutomationLogreport -o D:\AutomationLogreport\report --clean")
        # os.system(r"allure open D:\AutomationLogreport\report")

    def test_01(self):
        print('测试用例1.')

    def test_02(self):
        print("测试用例2.")

    def test_03(self):
        print("测试用例3.")

if __name__ == '__main__':
    pytest.main()