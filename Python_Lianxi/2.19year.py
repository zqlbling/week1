#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'''
输入某年某月某日，判断这一天是这一年的第几天？

什么是闰年：
    能被4整除且不能被100整除的为闰年。
    如2004年就是闰年,1900年不是闰年。
    世纪年能被400整除的是闰年,如2000年
'''

year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入天数："))
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0<month<=12:
    sum = months[month-1]
else:
    print("输入有误！")
sum += day

leap = 0
if(year%400==0)or(year%4==0)and(year%100!=0):
    leap = 1
if (leap==1)and(month>2):
    sum += 1
print("是第{0}天".format(sum))
