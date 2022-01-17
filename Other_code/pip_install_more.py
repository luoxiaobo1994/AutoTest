# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021/11/2 14:27

import os

file = r"C:\Users\luoxiaobo\requirements.txt"
with open(file) as f:
    contents = f.readlines()
ls = [con.split()[0] for con in contents]
for item in ls:
    try:
        os.system("pip install %s"%item)
    except:
        print("%s 库已安装或不存在。")