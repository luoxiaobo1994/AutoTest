# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2022/5/26 22:58
# Desc: 六种装饰器语法

"""
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
装饰器的使用方法很固定
先定义一个装饰器（帽子）
再定义你的业务函数或者类（人）
最后把这装饰器（帽子）扣在这个函数（人）头上
"""

# 定义一个基础装饰器
def decorator(func):
    def wrapper(*args,**kwargs):
        func()
    return wrapper


