#!/bin/bash/env python

temp = 'i'

while temp != "Q":
    temp = input('请输入一个整(输入Q结束程序):')
    int1 = int(temp)
    if int1 > 0:
        print("十进制 ->十六进制：%d->0x%x" % (int1,int1))
        print("十进制 ->八进制：%d->0o%o" % (int1,int1))
        print("十进制 ->二进制：%d->" % int1,bin(int1))
