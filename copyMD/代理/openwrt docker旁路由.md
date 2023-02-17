# openwrt docker

## 提要

我这里只有一台linux主机，单网口，一台路由器（但是不可以科学）。

需要让所有流量都走linux里面的openwrt接口。（实现各种操作）



## 正文

我的路由器网关192.168.0.1。子网掩码24位





**eth0是网卡名，根据具体情况更改配置**

```
# 开启混杂模式
ip link set  eth0 promisc on

docker network create -d macvlan --subnet=192.168.0.0/24 --gateway=192.168.0.1 -o parent=eth0 macnet
```

我的linux网络本机ip是：192.168.0.208



openwrt要设置为一个与本机ip不同的，且在同一个网段的

```
docker run -d \
--restart always \
--network macnet \
--privileged \
--name openwrt_lwl \
sulinggg/openwrt:x86_64 /sbin/init
```

**容器版本得与本机一致。**

## 容器内部配置



Openwrt容器内配置

```
vim /etc/config/network 
```

具体的配置

```
config interface 'loopback'
        option ifname 'lo'
        option proto 'static'
        option ipaddr '127.0.0.1'
        option netmask '255.0.0.0'

config globals 'globals'
        option packet_steering '1'

config interface 'lan'
        option type 'bridge'
        option ifname 'eth0'
        option proto 'static'
        option netmask '255.255.255.0'
        option ip6assign '60'
        option ipaddr '192.168.0.2'
        option gateway '192.168.0.1'
        option dns '8.8.8.8'

config interface 'vpn0'
        option ifname 'tun0'
        option proto 'none'
```





重启网络

```
/etc/init.d/network restart
```





然后就可以通过192.168.0.2访问openwrt了。

![image-20221113144733240](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/abc4bfe03679e22fabb51b8e9fb21bf4/76cf55cc1affeae22ac0fed3004002e5.png)





## 配置科学以及一些配置

做这个之前，先检查openwrt的网络是否通畅，我之前因为dns配置错了，导致一直没搞定。



就是clash，ssr









## 设置主路由的dhcp

让连接主路由的设备默认走旁路由网关

![image-20221113144137125](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/abc4bfe03679e22fabb51b8e9fb21bf4/8557371175b5879904b17864fb35bbe4.png)