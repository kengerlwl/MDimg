# Nginx配置

## Nginx的基本命令

```
nginx # 开启
nginx -s reload     #重新加载配置文件
nginx -s reopen     #重新打开log文件
nginx -s stop       #快速关闭nginx服务
nginx -s quit       #优雅的关闭nginx服务，等待工作进程处理完所有的请求
```

## 总体文件结构

```
user  root;  # 用户
worker_processes auto;
error_log  /www/wwwlogs/nginx_error.log  crit;
pid        /www/server/nginx/logs/nginx.pid;
worker_rlimit_nofile 51200;

events
    {
        use epoll;
        worker_connections 51200;
        multi_accept on;
    }

http
    {
        include       mime.types;
                #include luawaf.conf;

                include proxy.conf;

        default_type  application/octet-stream;

        server_names_hash_bucket_size 512;
        client_header_buffer_size 32k;
        large_client_header_buffers 4 32k;
        client_max_body_size 50m;

        sendfile   on;
        tcp_nopush on;

        keepalive_timeout 60;

        tcp_nodelay on;

        fastcgi_connect_timeout 300;
        fastcgi_send_timeout 300;
        fastcgi_read_timeout 300;
        fastcgi_buffer_size 64k;
        fastcgi_buffers 4 64k;
        fastcgi_busy_buffers_size 128k;
        fastcgi_temp_file_write_size 256k;
                fastcgi_intercept_errors on;

        gzip on;
        gzip_min_length  1k;
        gzip_buffers     4 16k;
        gzip_http_version 1.1;
        gzip_comp_level 2;
        gzip_types     text/plain application/javascript application/x-javascript text/javascript text/css application/xml;
        gzip_vary on;
        gzip_proxied   expired no-cache no-store private auth;
        gzip_disable   "MSIE [1-6]\.";

        limit_conn_zone $binary_remote_addr zone=perip:10m;
                limit_conn_zone $server_name zone=perserver:10m;

        server_tokens off;


# 访问日志配置在这

#自定义名为main得日志格式


log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';

access_log /www/wwwlogs/access.log    main;  # 这里是具体路径





# 这里是我们需要注意的东西，也是配置主要需要修改的东西
  server {

  #我们访问119.29.143.49：80
        listen       81;               # 端口
        server_name  110.40.204.239;    # 服务器名， 要代理的服务器的名字


        #存放静态资源的文件路径
         root   /root/front;


        #ngix的配置文件
        include /www/nginx/conf/*.conf;

        location / {
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
    



include /www/server/panel/vhost/nginx/*.conf;
}
```

一个Nginx文件可以有多个server模块，实现多个功能
## 代理静态资源


```
 server {
        listen       80;
        server_name  localhost; #服务器名字ip或者域名

        location / {
            root   html;
            index  index.html index.htm;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        } 
}  
```


## 关于location指令
location块指令会用其参数与客户端请求的URI进行匹配，匹配的URI请求会被定向到root指令定义的特殊本地文件系统目录中，重定向规则为：将URI添加到root参数后面，生成一个本地文件路径，即：root参数 + URI请求。这里示例参数”/”会匹配所有的请求，一般都会默认存在。示例定位后的目录为html/，默认是定位到安装目录的路径下的html/。这里location块指令内部的两个简单指令的含义是：



如下当访问http://anonymalias.oicp.net:8008/htdocs/，就会匹配到/home/anonymalias/htdocs/index.html



```
server {
        listen       80;
        server_name  localhost;

        location / {
            root   html;
            index  index.html index.htm;
        }

        location /htdocs {
            root   /home/anonymalias;
            index  index.html;
        }
}  

```

## 代理服务器
以下就是一个允许跨域访问的代理服务器配置
```
    server {
        listen       80;
        server_name  110.40.204.239;
        location / {
            add_header Access-Control-Allow-Origin '*' always;
            add_header Access-Control-Allow-Headers "Accept,Accept-Encoding,Accept-Language,Connection,Content-Length,Content-Type,Host,Origin,Referer,User-Agent";
            add_header Access-Control-Allow-Methods "GET, POST, PUT, OPTIONS";
            add_header Access-Control-Allow-Credentials true;
            if ($request_method = 'OPTIONS') {
                return 200;
            }
            
            proxy_pass  http://127.0.0.1:8000;
        }

    }

```
##### important
**proxy_pass：**
**一个nginx可以有多个location。
那么可以实现多个后端服务通过url前缀不同共用一个端口（如80）。**
该指令是反向代理的基本指令，用于设置代理服务器的协议和地址；对于一个client的请求，proxy_pass指令通过以下方式进行uri的转发：
- 如果proxy_pass指令的参数没有URI，那么请求的URI会被**原样的传递**给internal server。
- 如果proxy_pass指令的参数含有URI，client请求的URI匹配该location的部分将会被proxy_pass的path参数**替换**。
**例如：请求为127.0.0.1/name/index.html 会被转发为：127.0.0.1/remote/index.html**
```
location /name/ {
    proxy_pass http://127.0.0.1/remote/;
}
```


## 参考

[lin1](https://blog.csdn.net/anonymalias/article/details/50950910)