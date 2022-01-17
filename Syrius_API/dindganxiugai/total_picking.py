# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021/10/21 11:27

import pandas as pd
import os
from base.common import get_time


# 修改id的函数.
def add_id(file):
    df = pd.read_csv(file)
    # num = int(input("请输id入需要变化的量:"))  # 先默认+10了,其他先不动了.
    df.id += 10  # id这一列全变化.
    # print(df)
    df.to_csv(file, index=False, sep=',')


base_path = "D:\工作\项目\订单\近期常用"
file_ls = os.listdir(base_path)  # 目录下的订单文件
for item in file_ls:
    add_id(base_path + '\\' + item)  # 拼接文件路径,并增加id 10

print(get_time(),"修改完成!")
