# -*- coding:utf-8 -*-
# Author:Luoxiaobo
# Time: 2021/7/6 23:09

import string

def base_conversion():
    # a 原来的进制数，b 期望转化成的进制数。
    n,x,y = input("请连续输入，当前数值，当前数值的进制，期望转变的进制，以空格区分：").split(' ')
    ls = list(string.digits + string.ascii_uppercase)
    int_10 = int(n, int(x))
    s = []
    while True:
        s.append(ls[int_10 % int(y)])
        int_10 = int(int_10 / int(y))
        if int_10 == 0:
            break
    p = ''.join(s[::-1])
    print('{}进制数:{},转化为{}进制数为：{}'.format(x, n, y, p))
    return p

if __name__ == '__main__':
    base_conversion()