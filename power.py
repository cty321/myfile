#!/bin/bash/env python

def power(x,y):
    if (type(x) is int or type(x) is float) and (type(y) is int):
        temp = x ** y
    else:
        print('您输入有误，请重新输入！')

    return temp
    
