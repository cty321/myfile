#!/bin/env python

import itertools as its # 迭代器

words = "1234567890"
r = its.product(words,repeat=6)

# 打开一个文件，用于追加
file = open("pass.txt","a")

for i in r:
    file.write("".join(i))
    file.write("".join("\n"))
