# Python Redis，rabbitMQ以及Mysql使用操作教程
先redis

## Redis知识点
Redis的数据通常是存储在内存之中的，但是Redis支持数据的持久化，可以将内存的数据保存在磁盘中。
Redis 除了做缓存之外，也经常用来做分布式锁，甚至是消息队列。

### Redis 除了做缓存，还能做什么？
- 分布式锁 ： 通过 Redis 来做分布式锁是一种比较常见的方式。通常情况下，我们都是基于 Redisson 来实现分布式锁。相关阅读：《分布式锁中的王者方案 - Redisson》open in new window。
- 限流 ：一般是通过 Redis + Lua 脚本的方式来实现限流。相关阅读：《我司用了 6 年的 Redis 分布式限流器，可以说是非常厉害了！》open in new window。
- 消息队列 ：Redis 自带的 list 数据结构可以作为一个简单的队列使用。Redis5.0 中增加的 Stream 类型的数据结构更加适合用来做消息队列。它比较类似于 Kafka，有主题和消费组的概念，支持消息持久化以及 ACK 机制。
- 复杂业务场景 ：通过 Redis 以及 Redis 扩展（比如 Redisson）提供的数据结构，我们可以很方便地完成很多复杂的业务场景比如通过 bitmap 统计活跃用户、通过 sorted set 维护排行榜。



## 安装以及配置

1. 下载源码或者可执行文件地址[link](https://github.com/tporadowski/redis/releases)
2. 进行配置redis.conf文件（不同系统上可能有一定区别）
    2.1 添加密码：在文件中加入`requirepass 123456   #这个是密码`
    2.2 如果发现连接不上，需要修改redis.conf中的bind地址，bind意思是允许访问的主机：
            ```
            0.0.0.0：允许任意外部主机访问（推荐）
            127.0.0.1：只允许本机访问
            ```
3. 启动redis。在可执行文件目录下执行`redis-server.exe redis.windows.conf`
![](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/28ad227c312ac77ff864ee30af2ad98b/16e2c421d46d1fa0805f02ef701b9225.png)

4. 用redis的客户端查看
```
# 在服务器开始运行之后，运行命令
redis-cli.exe
```
![](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/28ad227c312ac77ff864ee30af2ad98b/70891fa074145dd529d88fb0e307b478.png)


5. 最终的配置文件
```

#这个是密码
requirepass 123456  

# 允许访问主机地址
bind 0.0.0.0 
```

## Python 进行连接使用

我们使用类`StrictRedis`。
```
from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='123456')
redis.set('name', 'GEJI')
print(redis.get('name'))
```


这样连接好后，就可以进行正常使用了。我们可以把redis当做一个离线的hashmap进行使用


总得来说，redis是比较灵活的。和python的map类似。里面可以有不同类型的value
- 键操作 
- 列表操作 
- 集合操作 
- 有序集合操作 
- 散列操作

### 过期
默认是永不过期


一些常见的函数操作可以参考[链接](https://cloud.tencent.com/developer/article/1151834)


# rabbitMQ使用操作教程

[rabbitmq的几大工作模式](https://xie.infoq.cn/article/02f4007cb22f991ee49882efa)

我这里已经把redis和rabbitmq打包到docker里面去了。
可以去pull下来



关于rabbitmq的启动：
```
/root/Lib/RabbitMQ/bin/rabbitmq-server start &  # 启动rabbitmq
/root/Lib/RabbitMQ/bin/rabbitmq-plugins enable rabbitmq_management & # 打开web服务界面

# 停止过服务
# rabbitmqctl stop

```

对rabbitmq进行用户添加以及设置权限分组
```

 rabbitmqctl add_user developer（用户名） 123456（密码） #新增用户以及密码
 
 rabbitmqctl delete_user developer  # 删除服务用户
 
 rabbitmqctl set_user_tags developer administrator（用户的权限组）#进行管理权限分组

rabbitmqctl set_permissions -p / developer（用户名） ".*" ".*" ".*" # 设置访问权限

```



## rabbitMQ的使用demo

send.py
```
# coding:utf-8
import pika

username = ''
password = ''
host = ''
credentials = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, credentials=credentials, port=5672))
channel = connection.channel()

channel.queue_declare(queue='qr_list',durable = True)

channel.basic_publish(exchange='',
                      routing_key='qr_list',
                      body='Hello World!')

print("[x] Sent 'Hello World!'")
connection.close()

```

revieve.py
```
# coding:utf-8
import pika
import time

username = ''
password = ''
host = ''

credentials = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=host, credentials=credentials, port=5672
))
channel = connection.channel()

channel.queue_declare(queue='qr_list',durable = True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    time.sleep(3)
    print(" [x] Done")
    # 确认消息
    ch.basic_ack(delivery_tag = method.delivery_tag)


if __name__ == '__main__':   
    channel.basic_consume('qr_list',callback,auto_ack = False)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
```




# mqsql 的安装使用
执行命令启动容器
```
docker run -it -p 0122:22 -p 6379:6379 -p 5672:5672 -p 15672:15672 --privileged centos_redis_and_rabbitmq init
解释：
-p： 进行端口映射
--privileged：优先级
init，设置/usr/sbin/init 为一号进程，方便后序的systemctl使用。
```

![](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/28ad227c312ac77ff864ee30af2ad98b/29245237bf8fe4e2b891c4bd15054ed0.png)


# docker compose使用
上面介绍的是三个服务装在一个docker容器里面运行，实际上这并不符合docker的运行规则。

docker的设计思路是每个容器运行一个程序，不同的程序分隔开来。

所以为了管理多个容器，引入了docker-compose。

这里简单讲讲我的配置文件吧。

## 首先有个文件目录如下
```
.
├── docker-compose.yml
├── mysql
│   ├── data
│   └── my.cnf
└── redis
    ├── data  
    └── redis.conf
#里面的两个data目录可以不用管，后面生成的
```

## 几个文件的配置
**mysql.my.cnf**
```
[client]
 port = 3306
 socket = /var/lib/mysql/data/mysql.sock
[mysqld]
 # 针对5.7版本执行group by字句出错问题解决
 sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'
 # 一般配置选项
 basedir = /var/lib/mysql
 datadir = /var/lib/mysql/data
 port = 3306
# Accept connections from any IP address
 bind-address	            = 0.0.0.0
 socket = /var/lib/mysql/data/mysql.sock
 lc-messages-dir = /usr/share/mysql # 务必配置此项，否则执行sql出错时，只能显示错误代码而不显示具体错误消息
 character-set-server=utf8
 back_log = 300
 max_connections = 3000
 max_connect_errors = 50
 table_open_cache = 4096
 max_allowed_packet = 32M
 #binlog_cache_size = 4M
 max_heap_table_size = 128M
 read_rnd_buffer_size = 16M
 sort_buffer_size = 16M
 join_buffer_size = 16M
 thread_cache_size = 16
 query_cache_size = 64M
 query_cache_limit = 4M
 ft_min_word_len = 8
 thread_stack = 512K
 transaction_isolation = REPEATABLE-READ
 tmp_table_size = 64M
 #log-bin=mysql-bin
 long_query_time = 6
 server_id=1
 innodb_buffer_pool_size = 256M
 innodb_thread_concurrency = 16
 innodb_log_buffer_size = 16M
```

**redis.redis.conf**
```
daemonize no     ## 若使用开机启动，生成pid，该项必须设置为诶yes，否则redis将不能够正常执行开机启动(systemctl start redis,执行后一直卡着，直到超时)

protected-mode no  ## 允许其他机器上的客户端连接当前redis，配置文件设置该项，则开机启动处就可以去掉--protected no 

#这个是密码
requirepass 123456

# 允许访问主机地址
bind 0.0.0.0 
```

**docker-compose.yml**

```
version: '3'
services:
  mysql:
    hostname: mysql
    image: mysql/mysql-server:5.7.26
    # network_mode: "host" # 如果需要容器使用宿主机IP(内网IP)，则可以配置此项,默认桥接模式
    container_name: mysql # 指定容器名称，如果不设置此参数，则由系统自动生成
    restart: always # 设置容器自启模式
    command: mysqld --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci # 设置utf8字符集
    environment:
      - TZ=Asia/Shanghai # 设置容器时区与宿主机保持一致
      - MYSQL_ROOT_PASSWORD=123456 # 设置root密码
    volumes:
       - /etc/localtime:/etc/localtime:ro # 设置容器时区与宿主机保持一致
       - ./mysql/data:/var/lib/mysql/data # 映射数据库保存目录到宿主机，防止数据丢失
       - ./mysql/my.cnf:/etc/mysql/my.cnf # 映射数据库配置文件
    ports:
        - "3306:3306"

  redis:  
    hostname: redis
    image: redis:5.0.4
    container_name: redis
    restart: always
    command: redis-server /etc/redis.conf # 启动redis命令
    environment:
      - TZ=Asia/Shanghai
    volumes:
      - /etc/localtime:/etc/localtime:ro # 设置容器时区与宿主机保持一致
      - ./redis/data:/data
      - ./redis/redis.conf:/etc/redis.conf
    ports:
        - "6379:6379"

  rabbitmq:
    image: rabbitmq:management-alpine
    container_name: rabbitmq
    environment:                      #设置用户名和密码
      - RABBITMQ_DEFAULT_USER=lwl
      - RABBITMQ_DEFAULT_PASS=123456
    restart: always
    ports:
      - "15672:15672"
      - "5672:5672"
    logging:
      driver: "json-file"
      options:
        max-size: "200k"
        max-file: "10"
```




## 运行与配置

在这个目录下运行`docker-compose -f docker-compose.yml up -d`


可以看到三个容器和镜像
```
❯ docker ps -a
CONTAINER ID   IMAGE                        COMMAND                  CREATED             STATUS                      PORTS     NAMES
67e41a460801   rabbitmq:management-alpine   "docker-entrypoint.s…"   About an hour ago   Exited (0) 14 minutes ago             rabbitmq
532bb3a9f99d   redis:5.0.4                  "docker-entrypoint.s…"   About an hour ago   Exited (1) 15 minutes ago             redis
ef1306403160   mysql/mysql-server:5.7.26    "/entrypoint.sh mysq…"   About an hour ago   Exited (0) 15 minutes ago             mysql
```

如果有哪个容器不对劲，按照之前的办法，可以通过`docker exec -it xxxxxxxx`命令去进行调试。

关于mysql没有链接上的问题,可以查看[link](https://blog.51cto.com/u_14349334/3485237)
```
GRANT USAGE ON *.* TO 'lwl'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
```


# docker compose的具体配置文件

具体参考详见[link](https://www.jianshu.com/p/2217cfed29d7)