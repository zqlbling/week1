#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# python正则表达式
# re.match尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
# 函数语法：
# re.match(pattern,string,flags=0)
# pattern匹配的正则表达式
# string要匹配的字符串
# flags标志位，用于控制正则表达式的匹配方式，
import re
print(re.match("www","www.4399.com").span())    # 在起始的位置匹配  (0, 3)
print(re.match("com","www.4399.com"))           # 不在起始位置匹配  None
