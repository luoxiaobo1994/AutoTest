# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021-07-08 14:33

# from pip._internal.utils.misc import get_installed_distributions
from subprocess import call
import os

""" 用于批量更新可更新的第三方库 """


def newway():
    model_ls = os.popen('pip list -o').readlines()  # 这样才能拿到命令行的返回值.
    # 第一行是名称,第二行是分割线
    up_list = [i.split()[0] for i in model_ls[2:-1]]  # 库信息的排布:'numpy  旧版本 新版本 xx' 按空格分割拿到包名就好
    try:
        up_list.remove('pip')  # 尽量不要更新pip，老容易出问题。 自己手动更新为好。
    except:
        pass
    print(f"可升级的库有:{up_list}")
    for item in up_list:
        if not item.startswith("\\x"):  # 抓到一个异常数据： '\x1b[0m'
            try:
                print('-' * 50, f'开始升级库:{item}', sep='\n')
                os.system(f"pip install --upgrade {item}")
            except:
                print(f"升级错误:{item}")


if __name__ == '__main__':
    newway()
