# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021-07-30 14:13
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from time import sleep

base_url = 'file:///D:/py_projects/Test_framework/Other_code/slder.html'

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get(base_url)
sleep(2)
slider = driver.find_element_by_id('dragEle')
slider_back = driver.find_element_by_class_name('tips')
# print(slider.size,slider_back.location, slider.location)
x_location = slider.location['x'] + slider_back.size['width']
y_location = slider.location['y']
AC(driver).click_and_hold(slider).perform()
x = 0
try:
    # while True:
    #     if x < 100:
    #         AC(driver).move_by_offset(xoffset=x, yoffset=0).perform()
    #         x += 1
    #     else:
    #         AC(driver).release().perform()
    #         break
    # ok_btn = driver.find_element(By.XPATH, '//input[@type="button"]')
    # ok_btn.click()
    # sleep(1)
    AC(driver).drag_and_drop_by_offset(slider,x_location,y_location).perform()
except:
    traceback.print_exc()

finally:
    time.sleep(5)
    driver.quit()
