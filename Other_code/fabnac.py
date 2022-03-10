# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/3/9 23:09


def fabnac(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fabnac(n-1) + fabnac(n-2)


print(fabnac(6))