#!/bin/bash/env python

def power(x,y):
    if y:
        return x * power(x,y-1)
    else:
        return 1

