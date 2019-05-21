#!/bin/bash/env python

def hui():
    c = 1
    hui = list(input('请输入一句话:'))
    b = len(hui)//2
    for i in range(b):
        if hui[i] == hui[-i-1]:
            c += 1
        else:
            return '不是回文联！'

        if c == b:
            return '是回文联！'


        
