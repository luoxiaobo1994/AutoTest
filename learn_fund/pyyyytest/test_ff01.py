# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/3/10 19:35
from time import sleep

import pytest

"""
关于fixture的补充,有参数:scope=[function:作用于函数,session:作用在类前和类后,就1次.]
autouse=[默认false,不会给类里的每个用例都套上,手动调用.True,每个用例都前后置执行]
params=[最好是列表，里面存了不同的参数值]，套件函数必须有参数request,函数通过yield request.param将参数传给用例函数。
        没有写错，fixture(params),这里面需要带s,yiled后面就不需要s了。一个参数，用例执行一遍。
        
如果要给类使用这个套件，则在类上面加上：@pytest.mark.usefixtures("套件函数名，不带括号")，如：
@pytest.mark.usefixtures("exe_sql")
class Test_fix():
---
要给整个package/session使用的话，一般结合conftest实现。

"""


@pytest.fixture()  # 使用这个装饰器,可以做成定制化的前置函数.给单独需要的用例进行装饰,达成个性化前置操作.
def exe_sql():
    print("操作数据库")  # 这是前置的部分.
    yield
    print("关闭数据库")  # 这是后置的部分.


@pytest.fixture(params=['lxb', 'lll', 'xxx'])
def use_param(request):
    print("开始使用套件")
    yield request.param
    print("结束使用套件")


class Test_ff():

    def setup_class(self):
        sleep(0.5)
        print("每个类之前,只执行1次的setup_class.")

    def teardown_class(self):
        sleep(0.5)
        print("每个类执行之后,才执行1次的teardown.")

    def setup(self):
        sleep(0.5)
        print("----------每个用例执行之前，都执行一次setup.-------------")

    def teardown(self):
        sleep(0.5)
        print("**********每个用例执行完成后，都执行一次teardown.********")

    def test_lxb(self):
        print("测试1:罗小波")

    def test_lxx(self):
        print("测试2:罗小波")

    def test_lx3(self):
        print("测试3:罗小波")

    # @pytest.mark.parametrize("user,password", [('user001', 123456), ('admin', 88888888), (None, 111), ('123', None)])
    # def test_login(self, user, password):
    #     print(f"user:{user},password:{password}")
    #
    # def test_fixture01(self, exe_sql):
    #     print("测试一下个性化前置.")
    #
    # def test_fixture02(self, use_param):
    #     print(f"使用了fixture的参数：{use_param}")


if __name__ == '__main__':
    pytest.main()