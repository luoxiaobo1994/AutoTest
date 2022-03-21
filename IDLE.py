# -*- coding:utf-8 -*-
# Author:Luoxiaobo
# Time: 2021/7/6 23:09


import random

list_1 = [89, 89, 62, 75, 62, 26, 75, 131, 75, 75, 62, 131, 26, 95, 95, 131, 62, 89, 89]
for i in list_1:
    # print(i)
    # print(list_1.count(i))
    if list_1.count(i)%2==1:
        print(i)
        break