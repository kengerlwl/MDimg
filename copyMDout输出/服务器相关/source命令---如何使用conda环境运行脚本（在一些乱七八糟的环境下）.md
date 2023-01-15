# 场景

最近写了一个python脚本。本来打算去宝塔里面整一个计划任务执行。

但是我测试的时候使用的环境是conda里面的python。

所以要让宝塔计划任务里面也使用该环境。



# 思路

### 法1

对于简单的，直接指定解释器的路径

```
/root/.conda/envs/main/bin/python3.7 test.py
```



### 法二

第一个办法对于涵盖有`sh`脚本的文件不是很友好。

使用，source激活指定环境。

```
source activate
conda activate main
bash sync_wordpress.sh 
```













## source命令的说明

`source filename`

source是bash shell的内置命令，用于**读取filename脚本文件中的命令**，**并在当前shell执行**。由于filename的执行环境是在当前shell，因此常用source命令在配置文件改变后，重新执行配置文件，避免重新登录。



### source和 sh，bash的区别

sh 会新建一个子shell，并在子shell中读取执行filename中的命令。**子shell会继承父shell的环境变量，但子shell中新生成的变量或者环境变化并不会传播到父shell中**，如需将新变量导入到父shell中，需使用export命令。







**活用好source命令，能够解决很多环境上的问题。**
