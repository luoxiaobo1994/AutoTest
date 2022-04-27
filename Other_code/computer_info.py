# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/4/21 13:50
# Desc:

import wmi

def system_info():
    pc = wmi.WMI()
    os_info = pc.Win32_OperatingSystem()[0]
    processor = pc.Win32_Processor()[0]
    os_name = os_info.Name.encode('utf-8').split(b'|')[0]
    ram = float(os_info.TotalVisibleMemorySize) / 1048576
    Gpu = pc.Win32_VideoController()[0]
    print(f"操作系统:{os_name}")
    print(f"CPU:{processor.Name}")
    print(f"内存:{ram:.2f} GB")
    print(f"显卡:{Gpu}")  # 独显是很长的一串信息.




if __name__ == '__main__':
    system_info()