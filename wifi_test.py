#!/bin/env python

import tkinter
import pywifi
from pywifi import const

# 判断当前是否链接到wifi
def gic():
    # 创建一个无线对象
    wifi = pywifi.PyWiFi()
    # 获取到无线网卡
    ifaces = wifi.interfaces()[0]
    # 打印无线网卡名称
    print(ifaces.name())
    print(ifaces.status())
    if ifaces.status() == const.IFACE_CONNECTED:
        print("连接成功")
    else:
        print("连接不成功")
    

gic()

# 扫描附近的wifi

def bies():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    #扫描wifi
    ifaces.scan()
    # 获取到扫描的结果
    bessis = ifaces.scan_results()
    print(bessis)
    for name in bessis:
        # 获取Wi-Fi的名称
        print(name.ssid)

bies()
