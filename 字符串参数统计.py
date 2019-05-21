#!/bin/bash/env python

str1 = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
int1 = '1234567890'

def count1(*var):
    ls = len(var)
    for i in range(ls):
        s = 0
        m = 0
        k = 0
        q = 0
        for x in var[i]:
            if x in str1:
                s += 1
            elif x in int1:
                m += 1
            elif x == ' ':
                k += 1
            else:
                q += 1
        print('第%d个字符串共有:英文字母%d个,数字%d个,空格%d个,其他字符%d个' % (i+1,s,m,k,q))
        
