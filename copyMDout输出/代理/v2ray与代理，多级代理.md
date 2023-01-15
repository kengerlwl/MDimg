# 代理与V2ray

参考：

[反向代理官方v2ray]( https://toutyrater.github.io/app/reverse.html)

## 正向代理

正向代理，实际上就是**翻墙的原理**

一般设置一个代理服务器，通过这个代理服务器去访问你想访问的网站，代理服务器就是客户端和目标服务器之间的跳板，代理服务器接收客户端的请求并发送到目标服务器，同时接收目标服务器的应答结果并返回给客户端，起到一个中介的作用。这就是所谓的正向代理。

**代理的是客户端**

使用v2ray配置，

**服务端：**

```
{

"log": {

"access": "/var/log/v2ray/access.log",

"error": "/var/log/v2ray/error.log",

"loglevel": "warning"

},

"inbounds": [

{

"port": 6688,   # 服务器端的用于接受客户端的接口

"protocol": "vmess",

"settings": {

"clients": [

{

"id": "8c042a38-71c1-1dcb-00df-54880236e0dc" # 客户端也要有这个id。

}

]

}

}

],

"outbounds": [

{

"protocol": "freedom"

}

]

}
```

客户端配置

![image-20220508111037368](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/8cb3d7627a138d3e74c02045c2347434/c6d740bf302d115132551cefdf25eeaa.png)



**注意：**

客户端和服务端时间要尽量保持一致







## 反向代理

反向代理是代理服务器，具体上是位于 Web 服务器前面的服务器，其将客户端（例如 Web 浏览器）请求转发到这些 Web 服务器。

比如如果我们客户端A要访问服务器C，不能直接访问，那么可以引入代理服务器B，让B去代理C，我们访问B就相当于访问C。

反向代理用于：

- 服务器负载均衡
- 防范服务器攻击
- 缓存
- 加密
- 内网穿透





**和正向代理不同的是：**

反向的代理代理的是服务器，所有服务器端的请求都可以走代理服务器

正向代理是代理的客户端，所有客户端都可以走代理服务器

![image-20220508112316782](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/8cb3d7627a138d3e74c02045c2347434/daa5afb33830ea1b0187d19056218a38.png)



### 服务器内网穿透

客户端

```
{  
  "reverse":{ 
    // 这是 A 的反向代理设置，必须有下面的 bridges 对象
    "bridges":[  
      {  
        "tag":"bridge", // 关于 A 的反向代理标签，在路由中会用到
        "domain":"private.cloud.com" // A 和 B 反向代理通信的域名，可以自己取一个，可以不是自己购买的域名，但必须跟下面 B 中的 reverse 配置的域名一致
      }
    ]
  },
  "outbounds": [
    {  
      //A连接B的outbound  
      "tag":"tunnel", // A 连接 B 的 outbound 的标签，在路由中会用到
      "protocol":"vmess",
      "settings":{  
        "vnext":[  
          {  
            "address":"110.40.204.239", // B 地址，IP 或 实际的域名
            "port":6688,
            "users":[  
              {  
                "id":"b831381d-6324-4d53-ad4f-8cda48b30811",
                "alterId":0
              }
            ]
          }
        ]
      }
    },
    // 另一个 outbound，最终连接本地的内网的服务 
    {  
      "protocol":"freedom",
      "settings":{  
      },
      "tag":"out"
    }    
  ],
  "routing":{   
    "rules":[  
      {  
        // 配置 A 主动连接 B 的路由规则
        "type":"field",
        "inboundTag":[  
          "bridge"
        ],
        "domain":[  
          "full:private.cloud.com"
        ],
        "outboundTag":"tunnel"
      },
      {  
        // 反向连接访问内网的规则
        "type":"field",
        "inboundTag":[  
          "bridge"
        ],
        "outboundTag":"out"
      }
    ]
  }
}
```

服务器

```
{  
  "reverse":{  //这是 B 的反向代理设置，必须有下面的 portals 对象
    "portals":[  
      {  
        "tag":"portal",
        "domain":"private.cloud.com"        // 必须和上面 A 设定的域名一样，可以是虚拟的
      }
    ]
  },
  "inbounds": [
    {  
      // 接受 C 的inbound
      "tag":"external", // 标签，路由中用到
      "port":80,
      // 开放 80 端口，用于接收外部的 HTTP 访问 
      "protocol":"dokodemo-door",
        "settings":{  
          "address":"127.0.0.1",
          "port":80, //假设 NAS 监听的端口为 80
          "network":"tcp"
        }
    },
    // 另一个 inbound，接受客户端主动发起的请求  
    {  
      "tag": "tunnel",// 标签，路由中用到
      "port":6688, //用于连接客户端的端口
      "protocol":"vmess",
      "settings":{  
        "clients":[  
          {  
            "id":"b831381d-6324-4d53-ad4f-8cda48b30811",
            "alterId":0
          }
        ]
      }
    }
  ],
  "routing":{  
    "rules":[  
      {  //路由规则，接收 C 请求后发给 A
        "type":"field",
        "inboundTag":[  
          "external"
        ],
        "outboundTag":"portal"
      },
      {  //路由规则，让 B 能够识别这是 A 主动发起的反向代理连接
        "type":"field",
        "inboundTag":[  
          "tunnel"
        ],
        "domain":[  
          "full:private.cloud.com"
        ],
        "outboundTag":"portal"
      }
    ]
  }
}
```



最后可以通过 **服务器ip：80**访问



## 多级代理提高溯源难度

如果就一台服务器，那么实际上通过查询那台服务器，可以找回到请求的原始ip。那么，可不可以在全球疯狂的绕几层服务器。大大提高服务器的溯源难度。

v2ray就可以。v2ray可以实现链式转发。

例如，如果有多个ssr账户，可以

```
{
  "outbounds": [
    {
      "protocol": "vmess",
      "settings": { // settings 的根据实际情况修改
        "vnext": [
          {
            "address": "1.1.1.1",
            "port": 8888,
            "users": [
              {
                "alterId": 64,
                "id": "b12614c5-5ca4-4eba-a215-c61d642116ce"
              }
            ]
          }
        ]
      },
      "tag": "DOUS",
      "proxySettings": {
          "tag": "DOSG"  
        }
    },
    {
      "protocol": "shadowsocks",
      "settings": {
        "servers": [
          {
            "address": "2.2.2.2",
            "method": "aes-256-cfb",
            "ota": false,
            "password": "password",
            "port": 1024
          }
        ]
      },
      "tag": "AliHK"
    },
    {
      "protocol": "shadowsocks",
      "settings": {
        "servers": [
          {
            "address": "3.3.3.3",
            "method": "aes-256-cfb",
            "ota": false,
            "password": "password",
            "port": 3442
          }
        ]
      },
      "tag": "AliSG",
      "proxySettings": {
          "tag": "AliHK"  
      }
    },
    {
      "protocol": "vmess",
      "settings": {
        "vnext": [
          {
            "address": "4.4.4.4",
            "port": 8462,
            "users": [
              {
                "alterId": 64,
                "id": "b27c24ab-2b5a-433e-902c-33f1168a7902"
              }
            ]
          }
        ]
      },
      "tag": "DOSG",
      "proxySettings": {
          "tag": "AliSG"  
      }
    },
  ]
}
```

那么数据包经过的节点依次为： PC -> AliHK -> AliSG -> DOSG -> DOUS -> 目标网站

这样的代理转发形成了一条链条，我称之为链式代理转发。

