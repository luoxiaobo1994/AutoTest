# -*- coding:utf-8 -*-
# Author: Luoxiaobo
# Time: 2021/7/18 16:22


import sys
import time

from tqdm import tqdm


def progress_bar():
    """ 普通进度条 """
    for i in range(1,101):
        print("\r",end="")  # 刷新在这行,为什么影响到下面的那条?  因为这是循环刷新,在循环里.把下面的每次刷新清除掉了.
        print("Download progress:{}%".format(i),"┃"*(i//2),end="")
        time.sleep(0.05)

def time_bar():
    """ 带时间的进度条 """
    scale = 50
    print("执行开始,祈祷不要报错".center(scale//2,'-'))
    start = time.perf_counter()  # ?
    for i in range(scale+1):
        a = '*' * i
        b = '.' * (scale-i)
        c = (i / scale) * 100
        dur = time.perf_counter() - start
        print("\r进度:{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end= '')
        time.sleep(0.1)
    print("\n万幸,执行成功.")

def tqdm_bar():
    for i in tqdm(range(1,500)):
        time.sleep(0.01)
    time.sleep(0.5)

if __name__ == '__main__':
    # progress_bar()  # 普通进度条
    # time_bar()
    tqdm_bar()