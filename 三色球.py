#!/bin/bash/env python

import random

qiu = [0,1,2,3,4,5,6,7,8,9,10,11]
hong = qiu[:3]
huang = qiu[3:6]
lv = qiu[6:]
int1 = 11

for i in range(7):
    qiu1 = random.randint(0,int1)
    if qiu[qiu1] in hong:
        print('红球')
    elif qiu[qiu1] in huang:
        print('黄球')
    elif qiu[qiu1] in lv:
        print('绿球')
    qiu.pop(qiu1)
    int1 -= 1
