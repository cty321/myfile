#!/bin/bash/env python

list1 = []

for x in range(10):
    for y in range(10):
        if x%2 == 0 and y%2 !=0:
            list1.extend([x,y])

list3 = [i:x[2:] for i in list2 for x in list1 if i[0] == x[0]]
