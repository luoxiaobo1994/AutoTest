# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/6/14 23:01
# Desc: 监听键盘事件


import time
import threading
import pynput.mouse
from pynput.keyboard import Key, Listener
from tkinter import *
import ctypes

LEFT = 0
RIGHT = 1

interval = 0.1


# 鼠标连点控制类
class MouseClick:
    def __init__(self, button, time):
        self.mouse = pynput.mouse.Controller()
        self.running = False  # 确认是否在运行
        self.time = time
        self.button = button
        # 开启主监听线程
        self.listener = Listener(on_press=self.key_press)
        self.listener.start()
        self.interval = 0.1

    def key_press(self, key):
        if key == Key.f8:
            if self.running:
                self.running = False
                state.delete('0.0', END)
                state.insert(INSERT, "当前状态: 监听中\n")
                state.insert(INSERT, "按下'ESC'键,退出监听\n")
                state.insert(INSERT, "按下'F8',停止连点.")
                # 停止连点也需要调用这个函数
                self.mouse_click()
            else:
                self.running = True
                state.delete('0.0', END)
                state.insert(INSERT, "当前状态: 点击中\n")
                state.insert(INSERT, "按下'F8',停止连点.\n")
                self.mouse_click()
        elif key == Key.esc:
            btn_start['state'] = NORMAL
            state.delete('0.0', END)
            state.insert(INSERT, "当前状态: 闲置\n")
            state.insert(
                INSERT, "选择需要连点的键,以及设置点击间隔时间, 点击开始按钮,开始连点.")
            # 退出主监听线程
            self.listener.stop()

    def mouse_click(self):
        # 这里还需要额外线程进行监听，为了能够更新self.running，防止陷入死循环
        key_listener = Listener(on_press=self.key_press)
        key_listener.start()
        while self.running:
            self.mouse.click(self.button)
            time.sleep(self.time)
        key_listener.stop()


# 新线程处理函数
def new_thread_start(button, time):
    MouseClick(button, time)


# START按键处理函数
def start():
    try:
        # 将文本框读到的字符串转化为浮点数
        interval = float(input.get())
        if mouse.get() == LEFT:
            button = pynput.mouse.Button.left
        elif mouse.get() == RIGHT:
            button = pynput.mouse.Button.right
        btn_start['state'] = DISABLED
        state.delete('0.0', END)
        state.insert(INSERT, "当前状态: 监听中\n")
        state.insert(INSERT, "按下'ESC'键,退出监听\n")
        state.insert(INSERT, "按下'F8',开始点击")
        # 开启新线程，避免GUI卡死
        t = threading.Thread(target=new_thread_start, args=(button, interval))
        # 开启守护线程，这样在GUI意外关闭时线程能正常退出
        t.setDaemon(True)
        t.start()
        # 不能使用 t.join()，否则也会卡死
    except:
        state.delete('0.0', END)
        state.insert(INSERT, "间隔时间设置错误!\n")
        state.insert(INSERT, "输入一个整数或者一个小数.")


# -------------------------------- GUI界面 --------------------------------
root = Tk()
# 高dpi
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor / 75)

root.title('简易连点器')
root.geometry('450x300')

mouse = IntVar()
lab1 = Label(root, text='鼠标按键选择', font=("微软雅黑", 11), fg="gray")
lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)
r1 = Radiobutton(root,
                 text='鼠标左键',
                 font=("微软雅黑", 10),
                 value=0,
                 variable=mouse)
r1.place(relx=0.05, y=40, relwidth=0.15, height=30)
r2 = Radiobutton(root,
                 text='鼠标右键',
                 font=("微软雅黑", 10),
                 value=1,
                 variable=mouse)
r2.place(relx=0.2, y=40, relwidth=0.3, height=30)

lab2 = Label(root, text='间隔时间(秒)', font=("微软雅黑", 11), fg="gray")
lab2.place(relx=0.55, y=10, relwidth=0.4, height=30)
var = StringVar(value=interval)
input = Entry(root, relief="flat", font=("微软雅黑", 10), textvariable=var)
input.place(relx=0.55, y=40, relwidth=0.4, height=30)

label3 = Label(root,
               text='---------- 当前状态  ----------',
               font=("微软雅黑", 8),
               fg="gray")
label3.place(relx=0.05, y=90, relwidth=0.9, height=20)
state = Text(root, relief="flat", font=("微软雅黑", 10))
state.place(relx=0.05, y=110, relwidth=0.9, height=120)
state.insert(INSERT, "当前状态: 闲置\n")
state.insert(INSERT,
             "选择需要连点的键,并设置间隔时间, 点击'开始'按钮,开始连点.")

btn_start = Button(root,  # 开始按钮
                   text='开始',
                   font=("微软雅黑", 12),
                   fg="white",
                   bg="#207fdf",
                   relief="flat",
                   command=start)
btn_start.place(relx=0.3, y=240, relwidth=0.4, height=30)

root.mainloop()
