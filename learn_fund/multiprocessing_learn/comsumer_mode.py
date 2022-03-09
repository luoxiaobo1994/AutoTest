# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/3/8 23:46

"""
队列是进程间交换数据最常用的方式之一，尤其适合生产者--消费之模式。multiprocess模块提供了一个queue.Queue近乎一模一样的Queue类。
它的put()和get()两个方法默认都是阻塞模式，这意味着一但队列为空，get()会被阻塞，一但队列满，则put()会被阻塞。 如果使用参数
block=False设置读写put()和get()为非阻塞，则读空或写满时会抛出异常。因此读写队列之前需要使用enmpy()或null()判断。
Queue类实例化时可以指定队列长度。
下面的代码，演示了典型的生产者--消费者模式。 进程A负责往地上扔钱，进程B则负责从地上捡钱。

"""
import os
import random
import time
import multiprocessing as mp


def sub_process_A(q):
    """ A进程函数：生成数据 """
    while True:
        time.sleep(5 * random.random())  # 在0~5s之间随机延时。
        q.put(random.randint(10, 100))  # 随机生成10~100之间的整数。


def sub_process_B(q):
    """ B进程函数：使用数据"""
    words = ['哈哈', '天哪', '卖狗的！', '咦，天上掉馅饼了？']
    while True:
        print("%s捡到了%d块钱" % (words[random.randint(0, 3)], q.get()))


if __name__ == '__main__':
    print("主进程(%s)开始，按任意键结束本程序。" % (os.getpid()))
    q = mp.Queue(10)  # 10个容量的队列。
    p_a = mp.Process(target=sub_process_A, args=(q,))
    p_a.daemon = True
    p_a.start()

    p_b = mp.Process(target=sub_process_B, args=(q,))
    p_b.daemon = True
    p_b.start()

    input()
