# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021/11/8 15:58

import requests
import json

#  用于下发订单任务.
requests_url = "https://gogoinsight-test.syriusrobotics.com/sz-test/1.0.58/index.html#/siteInfo?site=%5Bobject%20Object%5D"
data = {
        "timestamp":1639130389707,
        "expectedExecutionTime":1639130389707,
        "expectedFinishTime":1639130389707,
        "warehouseId":5,
        "id":"12989781",
        "batchId":"1",
        "type":"TOTAL_PICKING",
        "priority":"1",
        "storages":[
            {
                "type":"1A_container"
            }
        ],
        "items":[
            {
                "name":"医药外科口罩",
                "barcode":"6973291970458",
                "quantity":"15",
                "binLocations":[
                    "A01010104"
                ],
                "imageUrl":"file:///../sdcard/syrius_guanxi_productImg/4549395350520.png"
            },
            {
                "name":"可乐",
                "barcode":"6928804011142",
                "quantity":"10",
                "binLocations":[
                    "A05020101"
                ],
                "imageUrl":"file:///../sdcard/syrius_guanxi_productImg/4902777079851.jpg"
            },
            {
                "name":"雪碧   1L",
                "barcode":"6928804010145",
                "quantity":"1",
                "binLocations":[
                    "A04020204"
                ],
                "imageUrl":"file:///../sdcard/syrius_guanxi_productImg/4909384486567.png"
            },
            {
                "name":"罗小波 $%&^!&*  (",
                "barcode":"1546512",
                "quantity":"2",
                "binLocations":[
                    "A06020103"
                ],
                "imageUrl":"file:///../sdcard/syrius_guanxi_productImg/4923743543567.jpg"
            },
            {
                "name":"益达 木糖醇口香糖",
                "barcode":"6923450659861",
                "quantity":"4",
                "binLocations":[
                    "A07010201"
                ],
                "imageUrl":"file:///../sdcard/syrius_guanxi_productImg/4942355137139.png"
            },
            {
                "name":"消毒用 卫生湿巾",
                "barcode":"6931479600184",
                "quantity":"5",
                "binLocations":[
                    "A03010201"
                ],
                "imageUrl":"file:///../sdcard/syrius_guanxi_productImg/4571157254333.jpg"
            },
            {
                "name":"景田 饮用纯净水 350ml",
                "barcode":"6944649700058",
                "quantity":"5",
                "binLocations":[
                    "A02020204"
                ],
                "imageUrl":"file:///../sdcard/syrius_guanxi_productImg/4903301519393.png"
            }
        ]
    }

res = requests.request("post",url=requests_url,json=data)
# print(json.dumps(res.json()))