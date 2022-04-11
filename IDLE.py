# -*- coding:utf-8 -*-
# Author:Luoxiaobo
# Time: 2021/7/6 23:09

import traceback

try:
    print(1/0)
except:
    print(traceback.format_exc())