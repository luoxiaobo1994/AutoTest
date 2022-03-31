# -*- coding:utf-8 -*-
# Author:Luoxiaobo
# Time: 2021/7/6 23:09

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--nargs', nargs='+')
runner = 0
goal_list = ''
for _, value in parser.parse_args()._get_kwargs():
    if value is not None:
        print('Goals -', value)
        goal_list = value

print(goal_list)