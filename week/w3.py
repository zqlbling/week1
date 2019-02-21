#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
编写程序，生成一个包含20个随机整数的列表，
然后对其中偶数下标（下标即列表元素的索引）的元素进行降序排列，
奇数下标的元素不变。（提示：使用切片。）
'''

import random
list1 = []
for i in range(20):
    num1 = random.choice(range(100))
    list1.append(num1)

print("长度为：",len(list1))
print("排序前是：",list1)
list1[::2] = sorted(list1[::2],reverse=True)
print("偶数排序后是：",list1)