# -*- coding:utf-8 -*-
# Author:Luoxiaobo
# Time: 2021/7/6 23:09


import random
import string
ls = string.ascii_letters + string.digits + '~!@#$%^&*() '
print(len(ls))
ll = random.sample(ls,random.choice(range(0,63)))
print(''.join(ll))
