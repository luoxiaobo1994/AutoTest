# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021/12/1 21:03

file = "D:\pyproject\AutoTest\Other_code\data\score.txt"  # 文件地址。
d = {}  # 存储的字典
with open(file) as f:
    content = f.readlines()  # 把文件数据拿出来
# print(content)
for i in content:  # 循环遍历每一行数据
    score = i.replace('\n', '').split(' ')[1:]  # 分数部分，并把换行符替换掉
    d[i.split(' ')[0]] = sum(map(int, score)) / len(score)  # 名字做为键，把分数列表求平均。
name = input("请输入需要查询的：")
print(d.get(name, "查找的学生信息不存在，请检查输入信息。"))
