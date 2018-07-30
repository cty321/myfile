#!/bin/bash
if [ -e /etc/yum.repos.d/dvd.repo ];then
	echo "。。。。"
else
echo '[rhel7.4]
name=rhel7.4
baseurl=ftp://192.168.4.254/rhel7
enabled=1
gpgcheck=0' > /etc/yum.repos.d/dvd.repo
fi
yum -y install dhcp syslinux tftp-server httpd
mkdir /var/www/html/rhel7
mount -o loop /root/rhel-server-7.4-x86_64-dvd.iso /var/www/html/rhel7
echo '
subnet 192.168.4.0 netmask 255.255.255.0 {  #指定分配的网络
  range 192.168.4.10  192.168.4.150;       #指定分别的范围
  option domain-name-servers 192.168.4.7;   #指定DNS服务器地址
  option routers 192.168.4.254;          #指定网关地址
  default-lease-time 600;                
  max-lease-time 7200;
  next-server 192.168.4.7;   #指定下一个服务器IP地址
  filename  "pxelinux.0";    #指定网卡引导文件
} ' > /etc/dhcp/dhcpd.conf
mkdir -p /var/lib/tftpboot/pxelinux.cfg/
cp /usr/share/syslinux/pxelinux.0  /var/lib/tftpboot/
cp /var/www/html/rhel7/isolinux/isolinux.cfg  /var/lib/tftpboot/pxelinux.cfg/default
cp /var/www/html/rhel7/isolinux/vmlinuz  /var/lib/tftpboot/
cp /var/www/html/rhel7/isolinux/initrd.img  /var/lib/tftpboot/
cp /var/www/html/rhel7/isolinux/vesamenu.c32  /var/lib/tftpboot/
cp /var/www/html/rhel7/isolinux/splash.png  /var/lib/tftpboot/
mv /root/ks7.cfg /var/www/html/
sed -i '11c menu title my PXE Server' /var/lib/tftpboot/pxelinux.cfg/default
sed -i '70c append initrd=initrd.img  ks=http://192.168.4.7/ks7.cfg' /var/lib/tftpboot/pxelinux.cfg/default
systemctl start dhcpd
systemctl start httpd.service
systemctl start tftp
