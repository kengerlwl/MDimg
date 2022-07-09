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
while((true))
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







## my_shell_scropt

Openwrt network 检测

```
while((true))
do

sleep 60


# set try 2 times, and timeout is 1 second

net_out=$(ping -c 2 -i 1  baidu.com | grep ttl=)
if [ ! "$net_out" = "" ]
then
  echo "network exist, $net_out"
else
  echo "network fail"
fi

done
```

