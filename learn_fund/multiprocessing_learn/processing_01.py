# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/3/8 23:29

"""
1.Process原型：
p = multiprocessing.Process(group=None,target=None,name=None,args=(),kwargs={},*,daemon=None)
target是进程函数名，进程函数的函数通过args和kwargs传入。
2.Process的属性和方法：
方法/属性            说明
start()             启动进程，会自动调用p对象的run()方法
run()               启动进程时候自动运行的方法，去调用target指向的对象。如果需要自定义进程类，一定要实现run()方法.
terminate()         强制终止一个进程，不会做任何清理工作。如果P还有子进程，执行后子进程会成为僵尸进程。如果P有锁，则锁也不会清除，容易造成死锁。
is_alive()          判断进程p是否依然存在，如果是则返回True
join([timeout])     p的主线程等待p终止，timeout为可选的超时时间。主线程处于等待，而p处于执行状态。这个方法只适用于start()开启的进程，不能用于run()开启的进程
daemon              默认为False。如果设置为True，代表p是后台守护进程，如果p的父进程终止，p也终止。设置为True的时候，p无法创建新进程。这个参数必须在start()之前修改，进程开始运行后无法修改
name                获取进程名，默认是Process-n
pid                 获取进程的PID
exitcode            在运行的时候该值为None，如果进程结束了，表示被某个值的信号结束了进程
"""

import os, time
import multiprocessing as mp

def sub_process(name, delay):
    """进程函数"""

    while True:
        time.sleep(delay)
        print('我是子进程%s，进程id为%s'%(name, os.getpid()))

if __name__ == '__main__':
    print('主进程（%s）开始，按任意键结束本程序'%os.getpid())

    p_a = mp.Process(target=sub_process, args=('A', 1))
    p_a.daemon = True  # 设置子进程为守护进程
    p_a.start()

    p_b = mp.Process(target=sub_process, args=('B', 2))
    p_b.daemon = True  # 如果子进程不是守护进程，主进程结束后子进程可能成为僵尸进程
    p_b.start()

    input() # 利用input函数阻塞主进程。这是常用的调试手段之一。