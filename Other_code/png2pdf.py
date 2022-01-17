# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021/11/2 16:00

import os
from fpdf import FPDF
from base.common import get_time

pdf = FPDF()
pdf.set_auto_page_break(0)

path = r"E:\工作\项目\ponyrunner"
image_list = [i for i in os.listdir(path)]
print(f"共有{len(image_list)}张图片等待合成.")
count = 0
for image in sorted(image_list):
    count +=1
    pdf.add_page()
    pdf.image(os.path.join(path,image),w=180,h=270)
    print(f"{get_time()}完成第{count}张.")

pdf.output(os.path.join(path,"test.pdf"),"F")
