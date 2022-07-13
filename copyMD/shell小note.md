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

sleep 60


# set try 2 times, and timeout is 1 second

net_out=$(ping -c 2 -i 1  baidu.com | grep ttl=)
iw wlan1 info
if [ ! "$net_out" = "" ]
then
  echo "network exist, $net_out"
else
  send_msg
  echo "network fail"
fi

done
```



## Mac 常用的命令

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

