#!/bin/bash
if [ "$(yum repolist|awk '/^re/{print $2}')" -eq 0 ];then
echo '
[dvd]
name=rhel7
baseurl=ftp://192.168.4.254/rhel7
enable=1
gpgcheck=0' > /etc/yum.repos.d/dvd.repo
fi
tar -xf lnmp_soft.tar.gz -C /tmp
nginx1() {
echo "正在准备安装环境..."
yum -y install gcc openssl-devel pcre-devel > /etc/null
if [ -d /usr/local/nginx ];then
	echo "nginx OK"
elif [ -e /root/lnmp_soft.tar.gz ];then
	echo "nginx install......"
	cd /tmp/lnmp_soft 
	yum -y install php-fpm-5.4.16-42.el7.x86_64.rpm > /etc/null
	tar -xf /tmp/lnmp_soft/nginx-1.12.2.tar.gz > /etc/null
	cd /tmp/lnmp_soft/nginx-1.12.2/
	useradd nginx > /etc/null
	./configure --user=nginx --group=nginx --with-http_ssl_module > /etc/null
	make > /etc/null
	make install > /etc/null
fi
	sleep 1
	yum -y install mariadb mariadb-server mariadb-devel php php-mysql >/etc/null
	sleep 1
	ln -s /usr/local/nginx/sbin/nginx /sbin
	systemctl start mariadb
	systemctl start php-fpm
	sleep 1
	echo "安装完成。"
        sed -i '65,68s/#//' /usr/local/nginx/conf/nginx.conf
        sed -i '70,72s/#//' /usr/local/nginx/conf/nginx.conf
        sed -i '70s/\_params/\.conf/' /usr/local/nginx/conf/nginx.conf
	sed -i '20c fastcgi_buffers 8 16k;' /usr/local/nginx/conf/nginx.conf
	sed -i '20a fastcgi_buffer_size 32k;' /usr/local/nginx/conf/nginx.conf
	sed -i '21a fastcgi_connect_timeout 300;' /usr/local/nginx/conf/nginx.conf
	sed -i '22a fastcgi_send_timeout 300;' /usr/local/nginx/conf/nginx.conf
	sed -i '23a fastcgi_read_timeout 300;' /usr/local/nginx/conf/nginx.conf
	sed -i '40c keepalive_timeout  10;' /usr/local/nginx/conf/nginx.conf
	sed -i '25a gzip on;' /usr/local/nginx/conf/nginx.conf
	sed -i '26a gzip_min_length 1000;' /usr/local/nginx/conf/nginx.conf
	sed -i '27a gzip_comp_level 4;' /usr/local/nginx/conf/nginx.conf
	sed -i '28a gzip_types gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;' /usr/local/nginx/conf/nginx.conf
	nginx
}

nginx2() {
	echo "正在准备安装环境..."
	yum -y install gcc openssl-devel pcre-devel > /etc/null
	sleep 1
if [ -d /usr/local/nginx ];then
	echo "nginx OK"
elif [ -e /root/lnmp_soft.tar.gz ];then
	echo "nginx install......"
	cd /tmp/lnmp_soft 
	tar -xf /tmp/lnmp_soft/nginx-1.12.2.tar.gz > /etc/null
	cd /tmp/lnmp_soft/nginx-1.12.2/
	useradd nginx > /etc/null
	./configure --user=nginx --group=nginx --with-http_ssl_module --with-stream --with-http_stub_status_module > /etc/null
	make > /etc/null
	make install > /etc/null
fi
	ln -s /usr/local/nginx/sbin/nginx /sbin
	nginx
	echo "安装完成。"
}

tomcat() {
	echo "正在准备安装环境..."
	yum -y install java-*-openjdk java-*-openjdk-headless
	sleep 1
	cd /tmp/lnmp_soft
	tar -xf apache-tomcat-8.0.30.tar.gz 
	mv apache-tomcat-8.0.30 /usr/local/tomcat
	/usr/local/tomcat/bin/startup.sh
}

zabbix1() {
	echo "正在准备安装环境..."
	yum -y install net-snmp-devel curl-devel
	cd /tmp/lnmp_soft
	yum -y install libevent-devel-2.0.21-4.el7.x86_64.rpm php-bcmath-5.4.16-42.el7.x86_64.rpm php-mbstring-5.4.16-42.el7.x86_64.rpm
	yum -y install  php-gd php-xml
	tar -xf zabbix-3.4.4.tar.gz
	cd /tmp/lnmp_soft/zabbix-3.4.4/
	./configure --enable-server --enable-proxy --enable-agent --with-mysql=/usr/bin/mysql_config --with-net-snmp --with-libcurl
	sleep 1
	make && make install
	sleep 1
	yum -y install expect
	sleep 1
expect << EOF
	spawn mysql
	expect ">" {send "create database zabbix character set utf8;\r"}
	expect ">" {send "grant all on zabbix.* to  zabbix@'localhost' identified by 'zabbix';\r"}
	expect ">" {send "quit\r"}
EOF
	sleep 1
	cd /tmp/lnmp_soft/zabbix-3.4.4/database/mysql/
	mysql -uzabbix -pzabbix zabbix < schema.sql
	mysql -uzabbix -pzabbix zabbix < images.sql
	mysql -uzabbix -pzabbix zabbix < data.sql
	cd /tmp/lnmp_soft/zabbix-3.4.4/frontends/php/
	cp -r * /usr/local/nginx/html
	chmod -R 777 /usr/local/nginx/html/*
	sed -i "s/DBName=/DBName=zabbix/" /usr/local/etc/zabbix_server.conf
	sed -i "s/DBUser=/DBUser=zabbix/" /usr/local/etc/zabbix_server.conf
	sed -i "s#;date.timezone =#date.timezone = Asia/Shanghai#" /etc/php.ini
	sed -i "s/max_execution_time = 30/max_execution_time = 300/" /etc/php.ini
	sed -i "s/post_max_size = 8M/post_max_size = 32M/" /etc/php.ini
	sed -i "s/max_input_time = 60/max_input_time = 300/" /etc/php.ini
	useradd -s /sbin/nologin zabbix
	zabbix_server
	systemctl restart php-fpm
}

zabbix2() {
        echo "正在准备安装环境..."
        yum -y install gcc pcre-devel 
        cd /tmp/lnmp_soft
        tar -xf zabbix-3.4.4.tar.gz
        cd /tmp/lnmp_soft/zabbix-3.4.4/
        ./configure --enable-agent
	sleep 1 
	make && make install
        sleep 1
	cd misc/init.d/fedora/core
	cp zabbix_agentd /etc/init.d/
}
while :
do
echo "
	1.安装nginx服务器
	2.安装nginx调度
	3.安装tomcat-8
	4.安装zabbix监控服务器
	5.安装zabbix被控端
	6.exit
"
read -p "Input:" a

case $a in
1)
	nginx1;;
2)
	nginx2;;
3)
	tomcat;;
4)
	nginx1
	zabbix1;;
5)
	zabbix2;;
6)
	exit
esac
done










