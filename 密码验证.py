#!/bin/bash/env python

mima = input("请输入密码：")
mima1 = 'tiany'
chi = 3

while True:
    if '*' in mima:
        mima = input("密码中不能含有“*”号！您还有3次机会！请输入密码：")
    else:
        break
while chi > 0:
    if mima != mima1:
        mima = input("密码输入错误！您还有%d次机会！请输入密码：" % (chi - 1))
    else:
        print('密码正确，进入程序...')
        break
    chi = chi - 1
