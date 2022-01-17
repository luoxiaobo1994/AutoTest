# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021-08-12 11:18

import pymysql
import openpyxl

conn = pymysql.Connect(host='127.0.0.1',user='root',password='Lxb@12345',port=3306,db='python01',charset='utf8')
cur = conn.cursor()
sql = "select * from students"
cur.execute(sql)
data = cur.fetchall()
wb = openpyxl.Workbook()
wb.create_sheet('Sheet1')
sheet1 = wb['Sheet1']
for item in data:
    sheet1.append(list(item))
    wb.save('students.xlsx')
