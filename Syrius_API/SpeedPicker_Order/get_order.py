# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021/11/8 15:58

import requests

base_url = "https://gogoinsight-test.syriusrobotics.com/api/sz-test/order/warehouse-order?warehouseId=5"

res = requests.get(url=base_url)
print(res.text)