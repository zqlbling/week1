#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
1.分别输入两个字符串，输入两个字符串的拼接字符串（50分）
'''
str1 = input("请输入第一个字符串：")
str2 = input("请输入第二个字符串：")
str3 = str1+str2
print("您输入的两个字符串是：",str3)

'''
2.输入一个数字，将接收到的值转换为int类型，并打印该变量的类型。（50分）
'''
n = int(input("请输入一个数字："))
print("您输入的数字是：{0}".format(n))
print("您输入的数字类型是：{0}".format(type(n)))