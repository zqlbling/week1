#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
通过用户输入数字，计算阶乘
"""
num = int(input("请输入数字："))
def jc(num):
    if num==1:
        return 1
    else:
        return jc(num-1)*num
print("阶乘和是：",jc(num))



"""
判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
如果能被整除，则表明此数不是素数，反之是素数。
"""
for i in range(101,201):
    if i%2==0 or i%3==0 or i%5==0 or i%7==0:
        pass
    else:
        print(i)


"""
将一个列表的数据复制到另一个列表中，并反向排序输出
"""
list = [1,3,5,9,88,42]
list1 = []
for i in range(len(list)):
    list1.append(list[i])
print(list1[::-1])
