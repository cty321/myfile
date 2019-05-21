#!/bin/bash/env python

import random

int1 = random.randint(1,10)
time = 3
guess = 0

while guess != int1 and time > 0:
    temp = input("不妨猜一下小甲鱼现在心里想的是哪一个数字：")
    while not temp.isdigit():
        print("抱歉，输入不合法。",end='')
        temp = input("请输入一个整数：")
    guess = int(temp)
    if guess == int1:
        print('卧槽，你是小甲鱼心里的蛔虫吗？')
        print('哼～！猜中也没有奖励！')
        break
    elif guess > int1:
        print('大了！')
    elif guess < int1:
        print('小了！')
    time = time - 1
print('游戏结束，不玩了～！')
