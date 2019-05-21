#!/bin/bash/env python

def mybin(x):
    a = []
    if x == 1 or x == 0:
        return x
    else:
        return mybin(x//2)%2
    

