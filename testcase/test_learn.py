# -*- coding:utf-8 -*-
# Author: Luoxiaobo
# Time: 2021/7/18 10:21

import time
import pytest
from ddt import ddt,data,unpack

@ddt
class Test_learn():

    # @pytest.mark.run(order=4)
    def test_t1(self):
        """用例描述:这是用例1"""
        print("第一个测试用例T1")

    # @pytest.mark.run(order=3)
    def test_t2(self):
        print("第二个测试用例T2")

    # @pytest.mark.run(order=2)
    def test_t3(self):
        time.sleep(1)
        print("测试用例3,耗时操作")

    # @pytest.mark.run(order=1)
    def test_t4(self):
        """用例描述:执行顺序为1的用例."""
        time.sleep(1)
        print("测试用例4,耗时操作")

    @pytest.mark.skip
    def test_t5(self):
        """用例描述:这是一个被跳过的用例."""
        print("用例5:被标记跳过的用例,不会执行.")

    def test_t6(self,setUp):  # 把前置操作当成参数传入.
        """?"""
        print("用例6:有前置函数的.")

    @data([('1','2'),('3','4')])  # 有点问题
    @unpack
    # @pytest.mark.skip
    def test_t7(self,ar1,ar2):
        print(f"ar1:{ar1},ar2:{ar2}")

    @data('1','2','3')
    # @pytest.mark.skip
    def test_t8(self,ar1="默认"):
        print(f"参数ar1----->{ar1}")
        print("打印了吗????????????")


if __name__ == '__main__':
    # main函数的参数,是列表形式.列表里传字符串.
    """
    -v:运行的详细信息.
    -s:用例的打印信息.
    xx.py,指定运行的脚本.
    
    """
    1/0
    pytest.main(['./test_learn.py::Test_learn'])