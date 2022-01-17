# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021/10/20 12:28

while True:
    num = input("输入一个不超过5位的正整数:")
    if num.isdigit():
        if '-' in num:
            print("请输入正整数")
        else:
            print(f"{num}是一个{len(num)}位数.")
            print(f"翻转{num}的结果是:{num[::-1]}")
    else:
        print("输入类型不符,请输入数值.")