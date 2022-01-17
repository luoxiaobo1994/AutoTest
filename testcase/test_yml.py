# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021-07-23 16:57

from base.base_page import TestKey
from utils.config import Config
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
测试证明:这样不好使,yml得出来的结果是字符串.
By.XXX,这个部分,还是需要写到代码里.重新做判断.需要重构框架.
"""

fp = r'D:\py_projects\Test_framework\config\test_element.yml'
data = Config(fp)
print(eval(data.get('searchbtn')))
driver = TestKey(webdriver.Chrome())
driver.open_url('https://www.baidu.com')
driver.input_text(locator=data.get('inputbtn'),text='selenium')
driver.click_element(data.get('searchbtn'))
 