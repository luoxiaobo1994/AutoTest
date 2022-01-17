# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021-07-22 17:19

from appium import webdriver
import time
import threading
import os

app_tuya = {
    "platformName": "Android",
    "platformVersion": "7.1",
    "deviceName": 'emulator-5554',
    "apppackage": "com.tuya.smart",
    "appActivity": "com.tuya.smart/.hometab.activity.FamilyHomeActivity",  # 不能调起界面
    # "appActivity":"com.tuya.smart/com.smart.TuyaSplashActivity",# 不能调起界面
    "noReset": True,
    "unicodeKeyboard": False,
    "resetKeyboard": False
}

app_gncc = {
    "platformName": "Android",
    "platformVersion": "7.1",
    "deviceName": 'emulator-5556',
    "apppackage": "com.afar.gncc",
    "appActivity": "com.afar.gncc/.smart.home.activity.HomeActivity",
    "noReset": True,
    "unicodeKeyboard": False,
    "resetKeyboard": False
}

def task_tuya():
    os.system(f"adb -s {app_tuya['deviceName']} shell am start {app_tuya['appActivity']} ")
    time.sleep(5)
    os.system(f"adb -s {app_tuya['deviceName']} shell am force-stop {app_tuya['apppackage']}")
    print("命令关闭tuya,即将脚本启动.")
    time.sleep(5)
    # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',app_tuya)
    # time.sleep(5)
    # print('TUYA----',driver.contexts)
    # driver.quit()

def task_gncc():
    os.system(f"adb -s {app_gncc['deviceName']} shell am start {app_gncc['appActivity']} ")
    time.sleep(5)
    os.system(f"adb -s {app_gncc['deviceName']} shell am force-stop {app_gncc['apppackage']}")
    print("命令关闭GNCC,即将脚本启动.")
    time.sleep(5)
    # driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', app_gncc)
    # time.sleep(5)
    # print('GNCC----',driver.contexts)
    # driver.quit()

thread_ls = []
t1 = threading.Thread(target=task_tuya)
thread_ls.append(t1)
t2 = threading.Thread(target=task_gncc)
thread_ls.append(t2)

if __name__ == '__main__':
    for i in thread_ls:
        i.start()