# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/3/10 10:11

""" 一个关于BluePrint的自动化测试"""

from base.base_page import TestKey
import re
from time import sleep
from selenium.webdriver.common.by import By
from base.common import *
from utils.log import logger
from selenium.webdriver import Chrome, ChromeOptions


class BluePrint():
    options = ChromeOptions()
    options.add_argument("--start-maximized")

    def __init__(self):
        self.url = "https://gogoinsight-sqa-test.flexgalaxy.com/console/index.html"
        self.driver = TestKey(Chrome(options=BluePrint.options))

    def open_blueprint(self):
        """ 打开blueprint """
        self.driver.open_url(self.url)

    def login(self, user="lin82726142@163.com", password="123123Qq."):
        """ 登录 """
        try:
            self.driver.click_one(
                self.driver.find_element((By.XPATH, '//button[starts-with(@class,"el-button")]'), wait=15))
        except Exception as e:
            print(e)
            pass
        self.driver.input_text((By.XPATH, '//input[@id="login_account"]'), text=user)
        self.driver.input_text((By.XPATH, '//input[@id="login_password"]'), text=password)
        self.driver.click_element((By.XPATH, '//button[contains(@class,"login-form-button")]'))
        if self.driver.element_display((By.XPATH, '//*[@class="logout pointer"]'), wait=10):
            logger.debug("登录成功。")
            return
        logger.debug("登录失败")
        # 登录失败的提示
        # login_fail = self.driver.find_element((By.XPATH,'//div[@class="ant-form-explain"]'))

    def site_list(self):
        """ 场地列表 """
        site_list = self.driver.find_elements((By.XPATH, '//div[@class="item"]'))
        logger.debug(f"当前账户，包含了{len(site_list)}个场地。")

    def map_list(self):
        """ 地图列表 """
        self.driver.click_one(self.driver.find_elements((By.XPATH, '//li/div/span'))[1])
        map_list = self.driver.find_elements((By.XPATH, '//div[contains(@class,"el-card box-card")]'))
        logger.debug(f"当前账户，包含了{len(map_list)}张地图。")

    def app_manage(self):
        """ 管理的小程序 """
        self.driver.click_one(self.driver.find_elements((By.XPATH, '//li/div/span'))[2])
        """ 查看可管理的小程序 """
        app_list = self.driver.find_elements((By.XPATH, '////tr[contains(@class,"ant-table-row")]'))
        logger.debug(f"当前账户，可管理{len(app_list)}个小程序。")

    def enter_site(self, sitename=" sz-sqa-test "):
        self.driver.click_one(self.driver.find_elements((By.XPATH, '//li/div/span'))[0])
        self.driver.click_element((By.XPATH, f'//p[(text()="{sitename}")]'))

    def order_list(self, sitename=" sz-sqa-test "):
        """ 查看订单列表 """
        self.enter_site(sitename)
        total_order = self.driver.get_element_text((By.XPATH, '//span[@class="el-pagination__total"]'))
        logger.debug(f"当前场地:{sitename}，共有{len(total_order)}条数据。")

    def search_order_by_id(self, id='luoxiaobo', sitename=" sz-sqa-test "):
        """ 根据订单ID查询订单"""
        self.enter_site(sitename)
        input_element = self.driver.find_elements((By.XPATH, '//label[@title="Order ID"]/../..//input'), wait=5)
        input_element.send_keys(id)
        self.driver.click_element((By.XPATH, '//button[@class="ant-btn ant-btn-primary"]'))  # 切换语言可能会出问题。不建议写按钮的名称

    def search_order_by_batch(self, id='luoxiaobo', sitename=" sz-sqa-test "):
        """ 根据波次ID查询订单"""
        self.enter_site(sitename)
        input_element = self.driver.find_elements((By.XPATH, '//label[@title="Batch ID"]/../..//input'), wait=5)
        input_element.send_keys(id)
        self.driver.click_element((By.XPATH, '//button[@class="ant-btn ant-btn-primary"]'))  # 切换语言可能会出问题。不建议写按钮的名称

    def search_order_by_tote(self, id='199103181516', sitename=" sz-sqa-test "):
        """ 根据载物箱码查询订单"""
        self.enter_site(sitename)
        input_element = self.driver.find_elements((By.XPATH, '//label[@title="Tote Code"]/../..//input'), wait=5)
        input_element.send_keys(id)
        self.driver.click_element((By.XPATH, '//button[@class="ant-btn ant-btn-primary"]'))  # 切换语言可能会出问题。不建议写按钮的名称

    def search_order_by_slot(self, id='luoxiaobo', sitename=" sz-sqa-test "):
        """ 根据Slot码查询订单"""
        self.enter_site(sitename)
        input_element = self.driver.find_elements((By.XPATH, '//label[@title="Slot Code"]/../..//input'), wait=5)
        input_element.send_keys(id)
        self.driver.click_element((By.XPATH, '//button[@class="ant-btn ant-btn-primary"]'))  # 切换语言可能会出问题。不建议写按钮的名称

    def search_order_by_status(self, status="Executing"):
        self.driver.click_element((By.XPATH, '//label[@title="Order Status"]/../..//i'), wait=5)
        self.driver.click_element((By.XPATH, f'//li[@role="option" and text()="{status}"]'))  # 弹窗后可点。
        self.driver.click_element((By.XPATH, '//button[@class="ant-btn ant-btn-primary"]'))

    def search_order_by_business(self, status="Total picking"):  # picking可能会换为Picking
        self.driver.click_element((By.XPATH, '//label[@title="Business Process"]/../..//i'), wait=5)
        self.driver.click_element((By.XPATH, f'//li[@role="option" and text()="{status}"]'))  # 弹窗后可点。
        self.driver.click_element((By.XPATH, '//button[@class="ant-btn ant-btn-primary"]'))

    def check_config(self):
        self.driver.open_url(self.url + '?showConfig=1')
        self.login()
        self.enter_site()
        options = self.driver.find_elements((By.XPATH, '//div[@role="tab"]'))
        if len(options) == 5:
            logger.debug(f"检查配置成功，链接拼接配置之后，配置入口可见。")
            return
        logger.warning("检查一下，还是只有4个菜单选项")

    def change_language(self, language="English"):
        """ 切换语言 """
        self.driver.click_element((By.XPATH, '//a[starts-with(@class,"ant")]'))  # 整个页面只有一个a标签，只是为了避免以后有不一样的
        self.driver.click_element((By.XPATH, f'//li/a[contains(text(),"{language}")]'))

    def quit(self, timeout=3):
        # 临时的退出浏览器函数，后面用例化之后要去除。
        self.driver.quit(timeout)


if __name__ == '__main__':
    bp = BluePrint()
    bp.open_blueprint()
    bp.login()
    bp.change_language()
    bp.enter_site()
    bp.search_order_by_status()
    bp.quit()
