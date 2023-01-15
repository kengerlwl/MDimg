# 关于我在Ubuntu上配置route

## 前言



## 查看当前所有路由表，并进行管理

`ip rule list`输出所有的路由表

```
labot@core-labot:~$ ip rule list
0:	from all lookup local
32766:	from all lookup main
32767:	from all lookup default
```



新增路由表

修改**/etc/iproute2/rt_tables**

```
#
# reserved values
#
255     local
254     main
253     default
0       unspec
#
# local
#
#1      inr.ruhep
211     net_0 # 这是我们新增的路由表，前面的数据越小代表优先级越高。范围是0-255
```



但是并不代表一修改后就立刻可以通过ip rule查看到。

可能需要对该表新增一些路由配置后才能显示有

```
第1步：
  把路由表序号(10、11)和路由表名字(net_0、net_1)添加到/etc/iproute2/rt_tables中
第2步：
  （1）ip route add 192.168.2.0/24 dev eth0 src 192.168.2.10 table net_0
    从192.168.2.10发送到192.168.2.0/24网段的数据从eth0发出，把该路由项添加到路由表net_0中
  （2）ip route add default dev eth0 table net_0
    在路由表中添加默认路由，默认路由从eth0进出
  （3）ip rule add from 192.168.2.0/24 table net_0
    添加路由策略，来自192.168.2.10的路由要求使用net_0
  （4） ip route flush cache
    把新添加的路由策略和路由表刷新到缓存中，即时生效
```









## 关于路由表解释route -n

```
labot@core-labot:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.10.10.10     0.0.0.0         UG    0      0        0 ens160
0.0.0.0         10.10.10.10     0.0.0.0         UG    100    0        0 ens160
10.10.0.0       0.0.0.0         255.255.0.0     U     0      0        0 ens160
10.10.10.10     0.0.0.0         255.255.255.255 UH    100    0        0 ens160
10.11.0.0       0.0.0.0         255.255.0.0     U     0      0        0 ens192
172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 docker0
```

**destination 目的网段**
**[mask](https://so.csdn.net/so/search?q=mask&spm=1001.2101.3001.7020) 子网掩码**
**interface 到达该目的地的本[路由器](https://so.csdn.net/so/search?q=路由器&spm=1001.2101.3001.7020)的出口ip**
**gateway 下一跳路由器入口的ip**，路由器通过interface和gateway定义一调到下一个路由器的链路，通常情况下，interface和gateway是同一网段的
**metric 跳数，该条路由记录的质量**，一般情况下，如果有多条到达相同目的地的路由记录，路由器**会采用metric值小**的那条路由

### 一条条具体理解

```
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
# 缺省路由，如果目标网段找不到，那么就从这走。一般有default gateway决定。本例中，如果目标网段找不到，那么就从ens160设备，到10.10.10.10网关。交给网关去处理
0.0.0.0         10.10.10.10     0.0.0.0         UG    0      0        0 ens160
0.0.0.0         10.10.10.10     0.0.0.0         UG    100    0        0 ens160

#直联网段的路由记录，如果目的网段是10.10.0.0/16，那么从ens160出发，送到0.0.0.0。最后0.0.0.0又会发给10.10.10.10
10.10.0.0       0.0.0.0         255.255.0.0     U     0      0        0 ens160
10.10.10.10     0.0.0.0         255.255.255.255 UH    100    0        0 ens160
10.11.0.0       0.0.0.0         255.255.0.0     U     0      0        0 ens192
172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 docker0
```



### 和ip route的区别

显示格式不一样









## 路由表

**一个linux主机可以有多张路由表**

- 查看所有路由表

```
# in
ip rule

# out
0:      from all lookup local
32766:  from all lookup main
32767:  from all lookup default
# 可以看到有三张路由表，local，main，default。
# local：路由表 local 包含本机路由及广播信息。
# main：使用传统命令 route -n 所看到的路由表就是 main 的内容。
# default：default 路由表在默认情况下内容为空；除非有特别的要求，否则保持其内容为空即可。
```

- 删除一个路由表

```pf
ip rule del table out3 prio 32763
```

- 添加路由表

```pf
$ sudo echo "4 out4" >> /etc/iproute2/rt_tables
# 此时 ip rule 不能显示新增路由表
# 在新路由表添加应用规则后才能显示出来
# 给 out4 路由表添加应用规则： 来自 192.168.111.111 的数据使用 out4 路由表
$ sudo ip rule add from 192.168.111.111/32 table out4
```





## 一些route常见命令

```
    ip route show + 表名（et，main）：显示路由表； 

    ip route add：添加路由； 

    ip route append是追加   #追加一个指定网络的路由，为了平滑切换网关使用

    ip route change：修改路由；

    ip route replace：修改路由或添加路由；

    ip route delete：删除路由；

    ip route get：获得单条路由的详细信息；

    ip route flush：清空路由表；
    
```





## 关于ip route add/append 命令使用

```

sudo ip route append 10.10.0.0/16 via 0.0.0.0 dev ens160 src 10.10.114.32 protocol kernel  metric 100 table main
上面的意思是，到10.10.0.0/16这个范围的目的地，经过0.0.0.0 从src 10.10.114.32 出发，使用ens160网卡


- via 制定网关，经过哪
- dev 制定网卡
- src 源地址
- protocol  是该路由的路由协议标识符。proto kernel的意思是: 在自动配置过程中由内核安装的路由。
- metric 路由开销
- scope 指的是路由前缀覆盖的目标地址范围。 scope link表示在设备的网段内允许通过该路由进行通信
```





## SYS test

对ax3600添加默认路由，默认路由从ens192，且网关为10.11.11.11

```
sudo ip route add default dev ens192 via 10.11.11.11 table ax3600
```





给某个表添加路由策略

给10.10段添加路由

```
for((i=1; i<=3; i++));
do 
	sudo ip route append 10.10.0.0/16 dev ens160 src 10.10.110.3$i protocol kernel  metric 100 table main
done
```





给10.11段添加路由

```
for((i=1; i<=6; i++));
do 
	sudo ip route append 10.11.0.0/16 dev ens192 src 10.11.110.3$i protocol kernel  metric 101 table main
done
```



## ref

[route -n路由表理解](https://blog.csdn.net/yimenglin/article/details/107182098)

[路由表设置详解](https://segmentfault.com/a/1190000022752866)