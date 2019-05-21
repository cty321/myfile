#!/bin/bash/env python

def findstr():
    count = 0
    str1 = list(input('请输入目标字符串:'))
    str2 = input('请输入子字符串(两个字符):')
    for i in str1:
        if str2 in i:
            count += 1

    return print('子字符串在目标字符串中共出现%d次' % count)
