# -*- coding:utf-8 -*-
# Author:Luoxiaobo
# Time: 2021/7/6 23:09

import time,random


def random_time():
    x = [str(i).zfill(2) for i in list(time.localtime())]  # 时间戳
    x.append(str(random.randint(1, 1000)))
    # random.shuffle(x)  # 原地打乱列表顺序.
    y = int(''.join(x))  # 拼接,转型.
    print(y)

    return y

random_time()