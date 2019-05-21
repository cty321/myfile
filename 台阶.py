#!/bin/bash/env python

shu1 = input("台阶的倍数：")
shu2 = int(shu1)

while True:
    if (shu2*7)%2 == 1 and (shu2*7)%3 == 2 and (shu2*7)%5 == 4 and (shu2*7)%6 == 5:
        print("该台阶有%d阶" % (shu2*7))
        break
    else:
        print("错误，请重新输入！")
    shu2 = shu2 + 1
