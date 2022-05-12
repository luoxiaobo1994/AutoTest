# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/8 10:16
# Desc: 一个连点器

import win32con, win32api, ctypes
from threading import Thread
from keyboard import wait
from time import sleep


def clicker(x=0, y=0, lr=0):
    #  x,y 指定xy坐标，默认为0,0 鼠标的位置。
    # lr 0默认鼠标左键，1鼠标右键。
    if lr == 1:
        lr0, lr1 = win32con.MOUSEEVENTF_RIGHTDOWN, win32con.MOUSEEVENTF_RIGHTUP
    else:
        lr0, lr1 = win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP
    win32api.mouse_event(lr0 | lr1, x, y, 0, 0)

def clickers():
    while 1:
        # 循环点击鼠标左键单击
        clicker()
        sleep(0.25)

while 1:
    t = Thread(target=clickers)
    print("按下Ctrl+R开始连点。")
    wait("Ctrl+R")
    t.start()
    print("按下Ctrl+C停止连点")
    ctypes.pythonapi.PyThreadState_SetAsyncExc(t.ident,ctypes.py_object(SystemExit))
    t.join()
    sleep(1)
