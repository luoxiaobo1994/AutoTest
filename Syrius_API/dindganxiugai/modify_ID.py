# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021/10/26 11:44

import traceback
from pandas import read_csv
import time, openpyxl


# 时间戳
def get_time():
    now_time = time.localtime()  # [2020, 11, 30, 12, 3, 5, 0, 335, 0]
    date_1 = '-'.join(str(i).zfill(2) for i in now_time[:3])
    time_1 = ':'.join(str(i).zfill(2) for i in now_time[3:6])
    return date_1 + ' ' + time_1 + ' '


def change_id(file, num=100):
    if '.csv' in file:
        df = read_csv(file)
        df[df.columns[0]] += num  # 第一列，+100  #拿到第1列来写
        df.to_csv(file, index=False, sep=',')  # 避免写入索引列。
        print(get_time(), f'修改完成,所有ID增加{number}\n' + '-·' * 30 + '\n')
        return
    elif '.xlsx' in file:
        wb = openpyxl.load_workbook(file)  # 加载表格
        sheet1 = wb['Sheet1']  # 读取第一个工作表
        rows = sheet1.max_row  # 最大行数。
        for i in range(3, rows + 1):  # 序号是从1开始的，前两行是注释+表头。数据从3开始。还得多一个。
            try:
                old = sheet1.cell(row=i, column=1).value
                sheet1.cell(row=i, column=1).value = str(int(old) + 100)
            except:
                print("有非数字的订单ID，或者发送了其他异常。")
                print(traceback.format_exc())
        wb.save(filename=file)
        print(get_time(), f'修改完成,所有ID增加{number}\n' + '-·' * 30 + '\n')
        return
    else:
        print(get_time(), '传的什么鬼,检查一下,现在只支持csv和xlsx。')


if __name__ == '__main__':
    while True:
        file = input("将需要修改ID的订单拖至脚本区域:")
        try:
            number = 100
            if file:
                change_id(file, num=number)
            else:
                print("你传个空文件,我改什么?")
        except FileNotFoundError:
            print(f"{file}的路径错了,看看是不是多按了什么.")
        except:
            print(traceback.format_exc())
            print("出错了,重新上传一下.\n\n")
