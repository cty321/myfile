#!/bin/bash/env python

temp = input('请输入100-999的数字：')

while temp != '999':
    list1 = list(temp)
    if temp == "(int(list1[0]) ** 3) +  (int(list1[1]) **3) + (int(list1[2]) **3)":
        print('因此%s就是一个水仙花数' % temp)
    else:
        int1 = int(temp)
        int1 += 1
        temp = str(int1)
        continue
