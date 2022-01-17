# -*- coding:utf-8 -*-
# Author:Luoxiaobo
# Time: 2021/7/6 23:09

import os
import subprocess
import time
import traceback
from multiprocessing.dummy import Pool
import yaml
import re
from appium.webdriver import webdriver
from Syrius_UI.Shein_devices import devices
from utils.file_reader import YamlReader
import random
import string


ls = [1,1,1,1,11,1,1,0,1,1,1,]


def item_code(num=20):
    alpha = random.sample(string.ascii_letters, num // 3)
    number = random.sample('0123456789'*(num//10), num - num // 3)
    x = alpha+number
    random.shuffle(x)
    return ''.join(x)


print(item_code())
# print(item_code())