# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021-07-28 18:49
import pytest


@pytest.fixture()
def setUp():
    print("这是前置函数")

@pytest.fixture()
def tearDown():
    print("这是后置函数")