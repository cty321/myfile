#!/bin/bash/env python

year = input("输入一个年份：")

while not year.isdigit():
    print('抱歉，输入错误～！')
    year = input("输入一个年份：")

int1 = int(year)
if int1%4 == 0 and int1%100 != 0:
    print("%d是闰年" % int1)
else:
    print("%d不是闰年" % int1)
