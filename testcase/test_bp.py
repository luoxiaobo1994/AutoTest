# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/4/27 11:08
# Desc: BluePrint测试用例

import pytest
from pages.BluePrint import BluePrint
from selenium import webdriver

class Test_BluePrint():

    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.bp = BluePrint(cls.driver)
