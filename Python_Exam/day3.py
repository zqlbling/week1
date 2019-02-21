#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'''
1.输入两个人的生日，比较两个人年龄大小（50分）
'''
def MaxMin():
    year1 = int(input("请第一个人输入出生年份："))
    month1 = int(input("请第一个人输入出生月份："))
    day1 = int(input("请第一个人输入出生日期："))

    year2 = int(input("请第二个人输入出生年份："))
    month2 = int(input("请第二个人输入出生月份："))
    day2 = int(input("请第二个人输入出生日期："))

    if year1>year2:
        print("第二个人年龄大")
    elif year1==year2:
        print("两人同岁！")
    else:
        print("第一个人年龄大")
# MaxMin()
'''
2.随机生成一个序列，再次生成一个整数，查看这个整数有没有在序列中（50分）
'''
import random
a = random.randrange(1,31)
print(a)
