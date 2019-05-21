#!/bin/bash/env python

def sum1(x):
    a = 0
    for i in x:
        if (type(i) is int) or (type(i) is float):
            a += i
        else:
            continue

    return print(a)
