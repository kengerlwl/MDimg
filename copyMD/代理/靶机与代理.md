# docker 使用v2ray

思路：
- 校园网内一台机器，用来做跳板实现代理功能，这台电脑上安装v2ray服务器端代理，以及frpc客户端代理v2ray的入口到服务器
- 服务器就是frps。



# 目标靶机的v2ray配置

```
docker_name="v2ray-proxy"
docker stop ${docker_name}
docker rm ${docker_name}
docker run -it \
    --name ${docker_name} \
    -v $PWD/config/config.json:/etc/v2ray/config.json \
    -p 51223:51223 \
    v2fly/v2fly-core:v4.31.0
```

