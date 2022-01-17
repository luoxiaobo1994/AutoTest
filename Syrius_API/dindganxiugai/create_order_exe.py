# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/1/16 15:42

import tkinter as ttk


class Create_Order():

    def __init__(self):
        pass

    def init_widget(self):
        pass

    def create_order(self):
        "创建订单的主函数,一个按钮实现."

    def select_pick(self):
        """
        拣货类型:
        1.Total_picking
        2.Order_picking
        3.Sort after picking
        4.sort while picking
        5.预留一个其他选项.以后也许会修改字段.
        """
        pick_type = [
            "Total_Picking", "Order_Picking",
        ]


if __name__ == '__main__':
    app = ttk.Tk()
    user_text = ttk.Entry()
    user_text.pack()
    def get_text():
        user = user_text.get()
        print(user)
    ttk.Button(app, text="获取文本", command=get_text).pack()
    app.mainloop()
