# neo4j图数据库

这是一个知识图谱搭建并可视化的优秀平台



## 前置-------java环境安装

不同的neo4j版本对应不同的java环境。

**我这里选择的是neo4j 3.5 对应java版本java8**



所以要去安装java8.

以linux为例。

我这里选择下载可执行文件。然后从bashrc文件配置环境。



1、前往oracle Java官网下载JDK（http://www.oracle.com/technetwork/java/javase/downloads/index.html）

推荐华为镜像地址：https://mirrors.huaweicloud.com/java/jdk/

2、解压缩到指定目录（以jdk-8u191-linux-x64.tar.gz为例）

下载后解压。cd进去加入环境变量中。

```
#set oracle jdk environment
export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_191  ## 这里要注意目录要换成自己解压的jdk 目录
export JRE_HOME=${JAVA_HOME}/jre  
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib  
export PATH=${JAVA_HOME}/bin:$PATH 
```







## 安装neo4j

同样也是选择下载可执行文件的方式。

liunx环境[Neo4j](https://so.csdn.net/so/search?q=Neo4j&spm=1001.2101.3001.7020)下载地址：https://neo4j.com/download/other-releases/#releases(社区版免费)

解压

运行

```
./bin/neo4j start
```

然后有结果。

![image-20220905200159871](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/2970cc53434809d84eb89184b8668416/a3a551c9751930366f0511a069220dbe.png)

停止

进入bin目录执行./neo4j stop



查看图数据库状态

进入bin目录执行./neo4j status



客户端访问

http://服务器ip地址:7474/browser/

**在浏览器访问图数据库所在的机器上的7474端口（第一次访问账号neo4j，密码neo4j，会提示修改初始密码）**

