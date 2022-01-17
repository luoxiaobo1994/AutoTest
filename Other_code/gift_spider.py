# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021-08-09 18:05
import re
import requests
import time
from bs4 import BeautifulSoup
import csv
import os

q = "七夕礼物"
url_pattern = "https://s.taobao.com/search?q={}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20210805&ie=utf8&bcoffset=2&ntoffset=2&p4ppushleft=2%2C48&s={}"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62",
    # cookie值替换为使用上述方式获取的cookie值
    "cookie": "..."
}


def analysis(item, results):
    pattern = re.compile(item, re.I | re.M)
    result_list = pattern.findall(results)
    return result_list


def analysis_url(item, results):
    pattern = re.compile(item, re.I | re.M)
    result_list = pattern.findall(results)
    for i in range(len(result_list)):
        result_list[i] = result_list[i].encode('utf-8').decode('unicode-escape')
    return result_list


def precess(item):
    return item.replace(',', ' ')


# 创建csv文件
if not os.path.exists("gift.csv"):
    file = open('gift.csv', "w", encoding="utf-8-sig", newline='')
    csv_head = csv.writer(file)
    # 表头
    header = ['raw_title', 'view_price', 'view_sales', 'salary', 'item_loc', 'nick', 'detail_url', 'pic_url']
    csv_head.writerow(header)
    file.close()

for i in range(100):
    # 增加时延防止反爬虫
    time.sleep(25)
    url = url_pattern.format(q, i * 44)
    response = requests.get(url=url, headers=headers)

    # 声明网页编码方式，需要根据具体网页响应情况
    response.encoding = 'utf-8'
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    results = soup.find_all('script')
    information = str(results[7])

    # 获取所有的商品信息,由于有些购买人数为空白，导致返回空值，因此添加异常处理
    all_goods = analysis(r'"raw_title":"(.*?)"shopLink"', information)
    for good in all_goods:

        # 获取商品标题
        raw_title = analysis(r'(.*?)","pic_url"', good)
        if not raw_title:
            raw_title.append('未命名')
        # 获取商品价格
        view_price = analysis(r'"view_price":"(.*?)"', good)
        if not view_price:
            view_price.append('0.00')
        # 获取购买人数,由于有些购买人数为空白，导致返回空值，因此添加异常处理
        view_sales = analysis(r'"view_sales":"(.*?)"', good)
        # print(view_sales)
        if not view_sales:
            view_sales.append('0人付款')
        # 获取发货地址
        item_loc = analysis(r'"item_loc":"(.*?)"', good)
        if not item_loc:
            item_loc.append('未知地址')
        # 获取店铺名
        nick = analysis(r'"nick":"(.*?)"', good)
        if not nick:
            nick.append('未知店铺')
        # 获取详情页地址
        detail_url = analysis_url(r'"detail_url":"(.*?)"', good)
        if not detail_url:
            detail_url.append('无详情页')
        # 获取封面图片地址
        pic_url = analysis_url(r'"pic_url":"(.*?)"', good)
        if not pic_url:
            pic_url.append('无封面')
        with open('gift.csv', 'a+', encoding='utf-8-sig') as f:
            f.write(precess(raw_title[0]) + ','
                    + precess(view_price[0]) + ','
                    + precess(view_sales[0]) + ','
                    + precess(item_loc[0]) + ','
                    + precess(nick[0]) + ','
                    + precess(detail_url[0]) + ','
                    + precess(pic_url[0]) + '\n')
