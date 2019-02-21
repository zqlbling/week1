#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import time
now = time.time()
print("当前时间戳是：",now)    # UNIX和Windows只支持到2038年

localtime = time.localtime(time.time())
print("本地时间是：",localtime)

# 最简单的获取可读时间的时间模式的函数是asctime()
localtime = time.asctime(time.localtime(time.time()))
print("本地时间是：",localtime)   # Thu Feb 21 09:04:59 2019

# 格式化生成2019-03-21 09:05:24形式
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))  # 2019-02-21 09:06:57

# 格式化生成Thu Feb 21 09:04:59 2019的形式
print(time.strftime("%a %b %d %H:%M:%S %Y"),time.localtime())
# Thu Feb 21 09:30:55 2019 time.struct_time(tm_year=2019, tm_mon=2, tm_mday=21, tm_hour=9,
# tm_min=30, tm_sec=55, tm_wday=3, tm_yday=52, tm_isdst=0)

# 将格式字符串转换为时间戳
a = "Thu Feb 21 09:08:52 2019"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))) # 1550711332.0

import calendar
cal = calendar.month(2019,2)
print("以下输出2019年2月份的日历：")
print(cal)

# isleap(year) 查看year是否是闰年，是返回True，否则返回False
print(calendar.isleap(2019))

# leapdays(year1,year2) 返回year1-year2之间的闰年总数
print(calendar.leapdays(1980,2019))

import datetime
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)
