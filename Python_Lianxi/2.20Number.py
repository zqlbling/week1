#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 返回数字的绝对值
a1 = -10
print(abs(a1))

# 比较两个数的大小
print((10>9)-(10<9))    # 1

a3,a4 = 100,200
print(max(a3,a4))   # 返回给定参数的最大值
print(min(a3,a4))   # 返回给定参数的最小值

# 求x的y次方
print(pow(2,5)) # 32

# round(x[,n])  返回浮点数x 的四舍五入的值，如果n有值，代表四舍五入到后n位
print(round(3.456))
print(round(3.456,2))   # 保留两位小数

import math
# math.ceil()向上取整
# math.floor()向下取整
# math.sqrt()开方

# 返回整数部分与小数部分
print(math.modf(23.8))  # (0.8000000000000007, 23.0)

print(~10)  #-11

#eval(str)
#功能：将字符串str当成有效的表达式来求值并返回计算结果
num1 = eval("1234")
print(num1) # 1234
num1 = eval("-1234")
print(num1) # -1234
num1 = eval("12-4")
print(type(num1))
print(num1) # 8
# print(eval("a123"))

# lower()转换字符串为小写
str1 = "Good Good Study"
str2 = str1.lower()
print(str2) # good good study
print(str1) # Good Good Study
#转大写
print("Good Good Study".upper())    # GOOD GOOD STUDY
print(str1) # 又生成了一个新的字符串，原字符串不会改变

# zkill(width)返回一个长度为width的字符串，前面补“0”
str3 = "Good Good Study"
print(str3.zfill(40))
print(str3.ljust(20,"^"))

# lstrip() 方法用于截掉字符串左边的空格或指定字符。
# rstrip() 方法用于截掉字符串右边的空格或指定字符。
str4 = "*****Good Good Study*****"
print(str4.lstrip("*"))
print(str4.rstrip("*"))
print(str4.strip("*"))

num2 = 123
print(bin(num2))

print(9**1/2)

import datetime
now = datetime.date.today()
print(now)  #打印当前时间

                  # 19-02-20. 20 February 2019 is a Wednesday on the 20 day of February
date = now.strftime("%y-%m-%d. %d %B %Y is a %A on the %d day of %B")
print(date)

