# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/1/8 16:47

import os
import sys

def restrt_py():
    xx  = sys.executable
    args = sys.argv[:]
    os.execvp(xx,args)


print("开始")
try:
    for i in [1,4,2,1,4,0,2,0,5]:
        print(1/i)
except:
    restrt_py()

print("结束")
