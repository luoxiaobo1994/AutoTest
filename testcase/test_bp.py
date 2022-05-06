# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/4/27 11:08
# Desc: BluePrint测试用例

import pytest, os
from selenium.webdriver.common.by import By
from pages.BluePrint import BluePrint
from selenium import webdriver
from time import sleep


class Test_BluePrint():

    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.bp = BluePrint(cls.driver)
        cls.bp.open_blueprint()

    def teardown_class(cls):
        sleep(3)
        cls.driver.quit()

    @pytest.mark.parametrize('user,password', [('lin82726142@163.com', '123123Qq.')])
    def test_01_login(self, user, password):
        """ 正确的账户密码登陆 """
        self.bp.login(user, password)
        assert self.bp.element_display((By.XPATH, '//*[@class="logout pointer"]'))

    @pytest.mark.parametrize('user,password', [('xxx@163.com', '123123Qq.')])
    def test_02_login_failure(self, user, password):
        """ 错误的账户密码登陆 """
        self.bp.login(user, password)
        assert self.bp.element_display((By.XPATH, "//div[@*='ant-form-explain']"))


if __name__ == '__main__':
    pytest.main()
    os.system(r"allure generate D:\AutomationLogreport -o D:\AutomationLogreport\report.html --clean")
    # print(1)
