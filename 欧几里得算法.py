#!/bin/bash/env python

def gcd(x,y):
    int1 = x
    int2 = y
    while True:
        if x > y:
            temp = int1 % int2
            if temp == 0:
                return int2
                break
            else:
                int1 = int2
                int2 = temp
                temp = int1 % int2
        else:
            temp = int2 % int1
            if temp == 0:
                return int1
                break
            else:
                int2 = int1
                int1 = temp
                temp = int2 % int1
