# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/9 16:55
# Desc: allure的一些功能测试
import os

import allure
import pytest


def add(x, y):
    # 基础测试函数
    return x + y


@allure.severity(allure.severity_level.TRIVIAL)  # 严重等级:不重要
class TestAdd():  # 测试类

    @allure.title("用例标题:两个正数相加.")
    @allure.story("测试两个正数相加")
    @allure.severity(allure.severity_level.MINOR)  # 严重等级:轻微
    def test_first(self):
        """ 三个引号引起来的,会被记录为用例的描述性文本 """
        assert add(3, 4) == 7

    @allure.story("测试负数加正数")
    @allure.severity(allure.severity_level.NORMAL)  # 严重等级:一般/常规
    def test_second(self):
        assert add(-3, 4) == 1

    @allure.story("测试正数加负数")
    @allure.severity(allure.severity_level.CRITICAL)  # 严重等级:重要
    def test_three(self):
        assert add(3, -4) == -1

    @allure.story("测试错误的加法")
    @allure.severity(allure.severity_level.BLOCKER)  # 严重等级:中断
    def test_four(self):
        assert add(2, 2) != 2


if __name__ == '__main__':
    pytest.main()
    os.system(r"allure generate d:\tmp -o d:\report\ --clean")
