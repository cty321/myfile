#!/bin/bash/env python

def bin1(x):
    temp = []
    a = ''
    while x:
        b = x % 2
        x = x // 2
        temp.append(b)

    for i in temp:
        a = a + str('%s' % i)
        
    return print(a)
        
            
