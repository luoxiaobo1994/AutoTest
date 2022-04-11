# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/4/11 11:52
# Desc: 打印所有不超过n（取n<256）的其平方具有对称性质的数（也称回文数）。

if __name__ == '__main__':
    m = [1] * 17
    count = 0
    print(f"{'No.':<8}{'Number':<8}{'Square':<8}")  # 抬头
    for n in range(1, 256):  # 穷举n的值
        k, i, t, a = 0, 0, 1, n*n
        squ = a
        while a != 0:
            m[i] = a % 10
            a //= 10
            i += 1
        while i > 0:
            k += m[i-1] * t
            t *= 10
            i -= 1
        if k == squ and len(str(k))>2:
            count += 1
            print(f"{count:<8}{n:<8}{n*n:<8}")


