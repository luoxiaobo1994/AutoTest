# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/4/21 15:20
# Desc: webdriver一些常用属性练习
import datetime

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


# test_url: http://sahitest.com/demo/

class TTCase(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')

    def tt_weblement_prop(self):
        e = self.driver.find_element(By.ID,value='t1')
        print(type(e))
        print(e.id)
        print(e.tag_name)
        print(e.rect)
        print(e.size)




if __name__ == '__main__':
    tc = TTCase()
    tc.tt_weblement_prop()