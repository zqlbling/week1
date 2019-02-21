#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'''
用python语句判断所输入的手机号，是否正确
要对手机号的号段进行判断，号段任意给出6个作为模拟号段即可.
判断手机号码是否是由数字组成的
'''
# phone = input("请输入手机号：")
# list = [176,135,138,158,187]
# try:
#     int(phone)
#     if len(phone)==(11):
#         head = phone[0:3]
#         bool = False
#         for i in list:
#             if int(head)==(i):
#                 bool = True
#                 break
#         if bool:
#             print("输入正确")
#         else:
#             print("输入有误")
#     else:
#         print("手机号码长度不对！")
# except ValueError:
#     print("请输入正确的手机号！")












# phone = input("请输入手机号：")
# list = [189,187,168,176,133]
# try:
#     int(phone)
#     if len(phone)==11:
#         head = phone[0:3]
#         bool = False
#         for i in list:
#             if int(head)==i:
#                 bool = True
#                 break
#         if bool:print("输入正确")
#         else:print("输入有误")
#     else:print("请输入11位手机号")
# except ValueError:
#     print("请输入有效的手机号哦")















# 这是第三遍啦   不想敲了，呜呜

phone = input("手机号：")
list = [176,152,138,150,169]
try:
    int(phone)
    if len(phone)==11:
        head = phone[0:3]
        flag = False
        for i in list:
            if int(head)==i:
                flag=True
                break
        if flag:print("正确")
        else:print("错误")
    else:print("长度有误")
except ValueError:print("输入有误")