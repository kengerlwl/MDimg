## 目的

搭建一个多平台的文件同步系统。

无论是linux还是win，还是安卓什么的。





## Syncthing是啥

是一个开源的文件同步系统，性能非常优秀。

总体上来说是一个点对点的去中心化的同步系统。

如果在局域网内部，那么就会在内部网络做文件同步，很高效。也可以选择用公网服务器做同步，但是很消耗带宽。

推荐使用场景：

- 跨设备跨平台同步；比如 PC 端和移动端；
- 小范围（熟人间）资源共享；
- 企业内网之间多设备同步文件。





## 基于docker使用Syncthing做同步

Syncthing是一个类似frp的开远软件，如果直接基于源程序的方式去使用太不优雅的。而且版本管理，开机启动都要做管理，麻烦且没必要。

这里用docker新建一个Syncthing容器。

```
docker run --name syncthing -d -p 8384:8384 -p 22000:22000 -v 待同步的目录:/var/syncthing syncthing/syncthing
```

注意，因为使用docker，导致动态域名解析失败，因此，需要手动填入相应的域名（这里填的IP）。



### 先添加设备

![image-20221123221058166](/Users/lwl/Library/Application Support/typora-user-images/image-20221123221058166.png)

填入目标设备ID

![image-20221123221134471](/Users/lwl/Library/Application Support/typora-user-images/image-20221123221134471.png)

填入目标设备IP

![image-20221123221209755](/Users/lwl/Library/Application Support/typora-user-images/image-20221123221209755.png)





### 设置同的文件夹

不同设备间，这个标识符应该唯一

![image-20221123221257440](/Users/lwl/Library/Application Support/typora-user-images/image-20221123221257440.png)

设置待同步的设备

![image-20221123221333920](/Users/lwl/Library/Application Support/typora-user-images/image-20221123221333920.png)





### 主动扫描同步

![image-20221123221358020](/Users/lwl/Library/Application Support/typora-user-images/image-20221123221358020.png)

点击就会同步给共享中的设备。





## 一些技术实践的方案





### 通过公网服务器做中间节点

![image-20221124212741062](/Users/lwl/Library/Application Support/typora-user-images/image-20221124212741062.png)

要点：

- 通过服务器的同步服务关闭自动扫描，或者设置为只有每晚凌晨时候才扫描，因为服务器的带宽很小。
- 宿舍服务器用来做一个文件备份





### 直接内网穿透代理

为了解决不在局域网的情况，新增一个内网穿透22000端口呆公网。这样可以有效实现公网和内网穿插使用。





## 注意的坑点

### win一定要注意权限问题

如果你把目录建立在C盘根目录下面，那么很有可能导致没有写权限。

那么就会单方向导致文件同步失败。



