#!/bin/bash/env python

def gcd(x,y):
    if x % y == 0:
        return y
    else:
        return gcd(y,x%y)
