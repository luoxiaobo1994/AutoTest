# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021-07-19 16:07

import random

flag = True
while flag:
    anser = random.randint(1000, 10001)
    print('-'*25,'生成数字,游戏开始','-'*25)
    count = 1
    robot_max = 10000
    robot_min = 1000
    while count < 11:
        print("调试--答案是:", anser)
        result = input("输入你的数字,注意是四位数,输入quit结束游戏:")
        if result == 'quit':
            print("游戏结束,不玩咯~")
            flag = False
            break
        try:
            your_num = int(result)
            if len(str(your_num)) != 4:
                print("答案只是四位数,你输入的这个能对吗?")
        except:
            print('检查一下你的输入,真是数字吗?')
        robot_num = random.randint(robot_min,robot_max)
        res_ls = [your_num,robot_num]
        print(f"你的数字:{your_num},机器人的数字:{robot_num}")
        if your_num == robot_num == anser:
            print("恭喜,你和机器人都答对了.")
            break
        elif your_num == anser:
            print("恭喜,你赢了.")
            break
        elif robot_num == anser:
            print("抱歉,你没有答对,机器人答对了.")
            break
        else:
            print(f"你们都没有答对,继续猜,还有{10-count}次机会")
            count += 1
            if robot_num < anser < your_num:
                print('提示:你的大了,机器人的小了.')
                robot_max = your_num
                robot_min = robot_num
            elif robot_num <  your_num < anser:
                print('提示:你们俩的都小了.')
                robot_min = max(res_ls)
            elif anser < robot_num <  your_num:
                print("提示:你们俩的都大了.")
                robot_max = min(res_ls)
            elif your_num < robot_num < anser:
                print('提示:你们俩的都小了.')
                robot_min = max(res_ls)
            elif your_num < anser < robot_num:
                print('提示:你的小了,机器人的大了.')
                robot_max = your_num
                robot_min = robot_num
            elif anser < your_num < robot_num:
                print('提示:你们俩都大了.')
                robot_max = your_num
                robot_min = robot_num
            else:
                print('提示:你的小了,机器人的大了.')
                robot_min = your_num
                robot_max = robot_num

