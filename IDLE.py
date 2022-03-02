# -*- coding:utf-8 -*-
# Author:Luoxiaobo
# Time: 2021/7/6 23:09

import os
import subprocess
import time
import traceback
from multiprocessing.dummy import Pool

import pandas
import yaml
import re
from appium.webdriver import webdriver
from Syrius_UI.devices_pad import devices
from utils.file_reader import YamlReader
import random
import string
import  json
import pandas as pd


ls1 = ("Order ID (M)", "Batch ID (O)", "Business type (M)", "Business process (M)", "Priority (M)",
                "Container type (M)"
                , "Item name (M)", "Item code(M)", "Item image link (O)", "Item count (M)", "Bin location (M)",
                "Sequential execution (O)")
ls2 = (1,2,3,4,5,6,7,8,9,10,11,12)
dd = dict(zip(ls1,ls2))
print(dd)