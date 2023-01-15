## 变量

- 简单定义一个变量

```
url="http://c.biancheng.net"
website1='C语言中文网：${url}'
website2="C语言中文网：${url}"
echo $website1   
echo $website2
```

**单引号代表默认全是字符串**

**双引号代表会解析内部的变量**

- 将代码块的输出定义为变量

```
variable=$(command)
echo $variable
```

## 循环

```
# 方式一
for i in list:
do
shell_command
done

#方式二
for((i=1;i<=10;i++));  
do   
echo $(expr $i \* 3 + 1);  
done

# 方式三
while [ true ] 
do
echo test
done
```



## 判断if

```
# demo 如下
if  condition
then
   statement1
else
   statement2
fi

# 例子
if [ ! "$a" = "" ]

```



## 函数

```
# 手动输入读取参数类型
funWithReturn(){
    echo "这个函数会对输入的两个数字进行相加运算..."
    echo "输入第一个数字: "
    read aNum
    echo "输入第二个数字: "
    read anotherNum
    echo "两个数字分别为 $aNum 和 $anotherNum !"
    return $(($aNum+$anotherNum))
}
# 可以用这种方式捕获echo的内容。（也就说说可以echo结果然后捕获。）另一种方式是用全局变量
var1=$(funWithReturn)
echo " $var1"

# 输入参数型
funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73
```



## 各种括号以及方括号

https://blog.csdn.net/taiyang1987912/article/details/39551385



## my_shell_scropt

Openwrt network 检测

想来也是傻逼，网络都没了，怎么发送消息报错啊

```
#!/bin/bash

send_msg(){

wget --quiet \
  --method GET \
  --header 'cache-control: no-cache' \
  --header 'postman-token: d5c91d47-1f97-6f9a-735d-366f09451895' \
  --output-document \
  - 'http://110.40.204.239:5700/send_private_msg?user_id=2892211452&message=openwrt%20network%20wrong'
}


while((true))
do

sleep 120


# set try 2 times, and timeout is 1 second

net_out=$(ping -c 2 -i 1  baidu.com | grep ttl=)
# iw wlan1 info

if [ ! "$net_out" = "" ]
then
	net_ok
  #echo "network exist, $net_out"
else
date
  # restrat the network service
wifi down && wifi up   # 重启wifi
/etc/init.d/network restart  #重启网络进程
  send_msg
  echo "network fail"
fi

done
```

## grep 命令

我们知道grep命令是用来匹配输出的，但是普通的用法是看这行是否含有关键字或者符合正则表达式。

但是实际操作中经常碰到如果匹配到不仅仅输出该行，还有输出相邻的剩下的行。

**打印后面相邻**n行

利用`-A n`达到目的

**打印前面相邻**n行

利用`-B n`达到目的

**打印前后相邻**n行

利用`-C n`达到目的







## awk命令

空格输出多个变量

```
echo $(seq 1 9) | awk '{ print $5,$6,$7}' | while read a b c
```

指定分割符

```
awk -F ',' '{print $2, $3}' employee.txt
```

printf格式化输出

```
 pip list | awk -F ' ' '{printf("%s==%s\n", $1, $2)}' 
```







## sed 命令

```
#匹配行前加
sed -i '/allow 361way.com   /iallow www.361way.com' the.conf.file
#匹配行前后
sed -i '/allow 361way.com   /aallow www.361way.com' the.conf.file
```

**行前后添加**

```

在首行前插入一行
# sed -i '1i\AAA' aa.txt
在首行后插入一行
# sed -i '1a\AAA' aa.txt 

在尾行前插入一行
# sed -i '$i\AAA' aa.txt 
在尾行后插入一样
# sed -i '$a\AAA' aa.txt 


# 第n行前添加一行
# sed -i 'ni\AAA' aa.txt

```







## Mac /linux常用的命令

**大部分linux都能够直接用**

### caffeine 防止息屏命令

```
# 600000秒不息屏
caffeinate -u -t 600000
```



### 实时查看网络速度nload

```
# en0 代表的是设备，可以通过ip address查看哪些设备
nload device en0
```





### 定时执行

```

实例1：每1分钟执行一次myCommand
* * * * * myCommand
(分钟，小时，日，月，星期)

# 星期六的23点执行
0 23 * * 6 cmd


# 每小时的3,15分钟执行
3,15 * * * * myCommand

# 每小时的3到15分钟执行
3-15 * * * * myCommand

# 每小时的3到15分钟内，每隔3分钟执行一次
3-15/3 * * * * myCommand

```

- ***** 取值范围内的所有数字
- **/** 每过多少个数字
- **-** 从X到Z
- **，**散列数字



### 关于linux用户管理
查看所有用户
```
cat /etc/passwd
```

添加用户
```
useradd -d /home/test test  # 添加用户test，指定其home目录为/home/test
useradd -s /bin/bash -g group test # 添加用户test，指定用户组
```

删除用户
```
userdel -r test # 加入r是为了删干净，删除了用户和用户的配置文件
```

添加用户组
```
groupadd -g 101  g1  # 添加用户组g1,指定gid为101
```

删除用户组
```
groupdel g1
```





### 关于用户文件权限管理

#### **查看文件权限**

`ls -ahl`

假设我这里有一个用户kenger（1002），用户组files（1004）

显示的内容如下：

![image-20221020134132328](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/c53b935433a115d5732aa06e1e6ac8ac/bdd03cabe38c22bbb73f783161e8504d.png)

其中的kenger.txt表示属于kenger用户，files用户组。同组的具有rwx权限。

**- 10个字符确定不同用户能对文件干什么**

**- 第一个字符代表文件（-）、目录（d），链接（l）**

**- 其余字符每3个一组（rwx），读（r）、写（w）、执行（x）**

**- 第一组rwx：文件所有者的权限是读、写和执行**

**- 第二组rw-：与文件所有者同一组的用户的权限是读、写但不能执行**

**- 第三组r--：不与文件所有者同组的其他用户的权限是读不能写和执行**



#### 更改用户权限

建议用chmod =

chmod 改变文件或目录的权限

chmod 755 abc：赋予abc权限rwxr-xr-x

**chmod u=rwx，g=rx，o=rx abc**：同上u=用户权限，g=组权限，o=不同组其他用户权限

chmod u-x，g+w abc：给abc去除用户执行的权限，增加组写的权限

chmod a+r abc：给所有用户添加读的权限







### 自动输入y 确认





# docker 容器相关的命令

**一些容器没有su命令。**

安装的方式

```
-bash/zsh: su: command not found
 
#Debian
apt-get install util-linux
 
#Ubuntu
apt-get install util-linux
 
#Alpine
apk add util-linux
 
#Arch Linux
pacman -S util-linux
 
#Kali Linux
apt-get install util-linux
 
#CentOS
yum install util-linux
 
#Fedora
dnf install util-linux
 
#OS X
brew install util-linux
 
#Raspbian
apt-get install login
 
#Docker
docker run cmd.cat/su su
```

