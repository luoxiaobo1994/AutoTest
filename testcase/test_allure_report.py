# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021-07-23 17:24
import os
import pytest

class Test_Allure_report():

    def test_case1(self):
        """
        用例描述,这是测试用例1.
        """
        print("测试用例1")
        assert 1 == 1

    def test_case2(self):
        """测试用例2,这个是失败的测试."""
        print("测试用例2")
        assert 1 < 1

    def test_case3(self):
        print("测试用例3")
        assert 1 in [1,2,3,4,5]

    def test_case4(self):
        print("测试用例4")
        assert True

if __name__ == '__main__':
    pytest.main(['./test_allure_report.py'])
    os.system('allure generate ./temp -o ./report --clean')
