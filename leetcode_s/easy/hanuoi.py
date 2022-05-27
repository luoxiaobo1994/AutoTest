# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/27 0:02
# Desc: 汉诺塔问题

"""
透过现象去看问题根本/本质. 移动的目标还是:
最底层那个,和其余的盘(n-1)的移动问题.
总之,流程是这样的:
1.想方设法,将n-1个,从A经过C移动到B上面.
2.此时将最底层的那个,直接从A移动到C上.完成第一个目标.
3.剩余的(n-1)个,又变回了,将最底下那个,从B通过A移动到C.

"""


# sum = 0


def hanuoi(n, a, b, c):
    # global sum

    if n > 0:
        hanuoi(n - 1, a, c, b)
        print(f'{a}-->{c}')
        # sum += 1
        hanuoi(n - 1, b, a, c)
    # else:


# print(f"需要{sum}次移动")

hanuoi(4, 'A', 'B', 'C')
