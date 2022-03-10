# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/3/10 19:35

import pytest

"""
关于fixture的补充,有参数:scope=[function:作用于函数,session:作用在类前和类后,就1次.]
autouse=[默认false,不会给类里的每个用例都套上,手动调用.True,每个用例都前后置执行]
"""

@pytest.fixture()  # 使用这个装饰器,可以做成定制化的前置函数.给单独需要的用例进行装饰,达成个性化前置操作.
def exe_sql():
    print("操作数据库")  # 这是前置的部分.
    yield
    print("关闭数据库")  # 这是后置的部分.


class Test_ff():

    def setup_class(self):
        print("每个类之前,只执行1次的setup_class.")

    def teardown_class(self):
        print("每个类执行之后,才执行1次的teardown.")

    def setup(self):
        print(">>>每个用例执行之前，都执行一次setup.<<<")

    def teardown(self):
        print("-*-每个用例执行完成后，都执行一次teardown.-*-")

    def test_lxb(self):
        print("测试罗小波")

    @pytest.mark.parametrize("user,password", [('user001', 123456), ('admin', 88888888), (None, 111), ('123', None)])
    def test_login(self, user, password):
        print(f"user:{user},password:{password}")

    def test_fixture01(self, exe_sql):
        print("测试一下个性化前置.")

