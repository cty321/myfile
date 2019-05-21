#!/bin/bash/env python

int1 = input("请输入一个整数：")
int2 = int(int1)

while int2 > 0:
    print(int2 * ' ' + int2 * '*')
    int2 = int2 - 1
