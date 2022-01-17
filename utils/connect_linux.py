# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/1/4 23:36
import time

import paramiko
from utils.log import logger

devices = {
    '10.111.150.201': '10.111.150.37',  # 501
    '10.111.150.104': '10.111.150.22',  # 404
    '10.111.150.108': '10.111.150.19',  # 408
    '10.111.150.205': '10.111.150.39',  # 505
    '10.111.150.203': '10.111.150.33',  # 503
    '10.111.150.204': '10.111.150.43',  # 504
    '10.111.150.102': '10.111.150.24',  # 402
    '10.111.150.212': '10.111.150.34',  # 512
    '10.111.150.111': '10.111.150.20',  # 411
    '10.111.150.202': '10.111.150.31',  # 502
    '10.111.150.206': '10.111.150.44',  # 506
    '10.111.150.216': '10.111.150.29',  # 516
    '10.111.150.209': '10.111.150.32',  # 509
    '10.111.150.121': '10.111.150.12',  # 421
    '10.111.150.106': '10.111.150.23',  # 406
    '10.111.150.193': '10.111.150.40',  # 493
    '10.111.150.210': '10.111.150.42',  # 510
    '10.111.150.125': '10.111.150.17',  # 425
    '10.111.150.211': '10.111.150.38',  # 511
    '10.111.150.215': '10.111.150.46',  # 515
    '10.111.150.195': '10.111.150.36',  # 495
    '10.111.150.208': '10.111.150.30',  # 相机坏了，不要用
    '10.111.150.207': '10.111.150.35',  # 507
    '10.111.150.117': '10.111.150.14',  # 417
    '10.111.150.213': '10.111.150.41',  # 513
    '10.111.150.214': '10.111.150.45'  # 514
}


def ssh(ip, cmds=[], username='syrius', password="syrius", port=22, i=False):
    client = paramiko.SSHClient()
    try:
        # 创建ssh客户端
        # 第一次ssh远程连接时，会提示输入yes或no
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 密码方式远程连接
        client.connect(ip, username=username, password=password, timeout=3)
        logger.debug(f"{ip}:{port}\t连接成功。")
        # 互信方式远程连接，没用到过，暂时屏蔽了。先保留代码,以后也许会用上.
        # key_file = paramiko.RSAKey.from_private_key_file('输入你的文件路径')
        # ssh.connect(syr_ip)
        # 执行命令
        if cmds:  # 有时候不执行命令.
            for command in cmds:
                print(f"执行命令:{command}")
                # 命令的输入和输出流以类似于Python file的对象的形式返回，它们代表stdin，stdout和stderr。
                stdin, stdout, stderr = client.exec_command(command, bufsize=-1,
                                                            timeout=3, get_pty=False, environment=None)
                # 读取执行命令后输出的内容
                out = stdout.readlines()  # 不执行输出,有些命令居然执行不成功,妈的.
                if i:  # 控制一下,是否打印消息.
                    for m in out:
                        print(m)
                time.sleep(1)  # 执行一条命令,等待一下,多线程,倒是无所谓了.
        return 1
    except Exception as e:
        logger.warning(f"{ip} {e}")
        return 0
    finally:
        client.close()


if __name__ == '__main__':
    # cmds = ["adb devices", "adb tcpip 5555"]
    # cmdss = ['killall navigation_skill',"adb devices", "adb tcpip 5555"]
    cmdss = ['tar xvf /etc/syrius/config_tree.tar.gz']
    # for i in devices.keys():
    for i in devices.keys():
        ssh(ip=i, cmds=['rm -rf ~/lxb', 'rm ~/lxb.tar.gz'])
