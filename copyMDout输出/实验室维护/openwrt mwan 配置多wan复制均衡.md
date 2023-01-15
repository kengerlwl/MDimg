## openwrt新建多个wan口

- 可以采取多线多口的方式。多个物理接口对应多个wan口
- 或者采取单线多拨的方式，但是运行商不一定支持。
  - 在单个网卡上虚拟出多个网卡
  - 不同网卡不同的ip，mac





## mwan配置复载均衡

mwan是一个openwrt上的插件，可以实现多wan口的上网流量管理。



**前置wan注意点**

![image-20221123161720081](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/daa0b5992d6a9fb3beceed9958bce7d2/eda6e16df827df14aad0155101d03f09.png)

- 网关跳跃点必须要有且不能重复





**配置mwan**

主要分为

![230293745_2_20210913102146914](/Users/lwl/Desktop/230293745_2_20210913102146914.jpg)





中文界面如图

![image-20221123162109769](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/daa0b5992d6a9fb3beceed9958bce7d2/edb606a7224ab98ef8d1f4882b10fa20.png)





**如何查看mwan的界面情况**

![image-20221123162154984](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/daa0b5992d6a9fb3beceed9958bce7d2/5a80cbdc331c819ef110d686b3e7077d.png)

在这个界面可以看到各个接口的在线情况





## 一套成熟的校园网多wan部署方案

### 需求

- 实现多个wan口
- 每个wan口都需要账号登录脚本使用指定参数做断开重连
- 将多个wan口聚合，做负载均衡提高网速





### 1先弄出多个wan口





### 2配置mwan的基本参数

包括接口，成员，策略



**不过这里策略多出了一些单wan口直连的，用于后序的网络断开重连维护**

![image-20221123162711423](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/daa0b5992d6a9fb3beceed9958bce7d2/6a0de772c0c3d8ef3ba274aa238c7f57.png)





### 3配置流量规则

**为了实现不同的wan口分别发起请求做断开重连维护。**

**我们需要将断开重连的的请求分别从不同的脚本发出去。**

**一个思路是，一台lan口下面的linux主机上，配置不同的ip。将不同的ip通过不同的wan口发送出去。**

**要做到这点，需要mwan配置openwrt上的流量规则。同时也要在linux上通过脚本指定ip发起请求。**

**我这里用的python指定发送脚本。后序程序会贴在附录。**



**主要分为以下规则**

- 从某个ip发送出的请求只走某个wan口。
- 将正常ip下的请求全部负载均衡。

如图

![image-20221124131230129](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/daa0b5992d6a9fb3beceed9958bce7d2/739fa6efefb433250b8cb44812f60ff6.png)







## 坑点

因为我这里需要另外一台局域网内的linux主机来通过指定wan口发起请求来实现断网重连。

那么意味着需要在断网情况下也能通过wan口访问。

但是mwan有个问题，就是如果断网时候，该wan口会自动下线，也就是说不能访问，这个坑我踩了好久。

**所以要么关闭wan口下线的功能**

**要么设置让两个wan口永远在线**



### 坑点之-------python的requests访问百度做判断并不准确

所以实用ping指定ip做判断

```
def net_check_ping(ip):

    cmd = 'ping -I {} -c 5 baidu.com'.format(ip)

    ans = os.system(cmd)
    if ans == 0:
        return True
    else:
        return False
```









## 附录



### python指定ip发起请求脚本

```python
import json
import http.client
import urllib.parse


def http_client():
    params = {"a": "123"}
    headers = {"Content-type": "application/json"}
    conn = http.client.HTTPConnection(
        "目标ip或者域名", 5000, source_address=("指定本地的ip", 0))
    conn.request("GET", "/") #发起特定请求
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read().decode()
    print(data)
    conn.close()


def main():
    http_client()


if name == 'main':
    main()
```

**或者用requests**

```
import random
import requests
from requests_toolbelt import SourceAddressAdapter


class SourceAddressRequests(object):
    def __init__(self):
        self.session = requests.session()
        self.ips = ['192.168.1.209', '192.168.1.210']

    def adapter_requests(self, ip):
        """随机绑定一个本机ip"""
        bind_address = ip
        print("请求ip：", bind_address)
        new_source = SourceAddressAdapter(bind_address)
        self.session.mount('http://', new_source)
        self.session.mount('https://', new_source)

    def test_requests(self):
        """测试请求"""
        url = "http://httpbin.org/get"
        response = self.session.get(url=url)
        origin = response.json()["origin"]
        print("检测到ip：", origin)

    def main(self):

        for i in range(len(self.ips)):
            self.adapter_requests(self.ips[i])
            self.test_requests()


    # 使用指定ip发起get请求
    def get_by_ip(self, url, headers):
        response = self.session.get(url=url, headers=headers)
        return response


if __name__ == '__main__':
    test = SourceAddressRequests()
    test.main()
```

**可以用重写直接替换get，在一定程度上达到无缝衔接的效果。**

```
# ip bind get write again
adapter = SourceAddressRequests()
requests.get = adapter.get_by_ip
```



### 在宿舍内的一些openwrt上需要配置的路由表


在宿舍内，如果openwrt某个wan断网了，那么当重新连接时，目标验证网站10.1.1.1根本ping不通。我猜是openwrt上没搞清楚这个要走那个口出去，初步判定，因为我这里涉及不通的运营商，所以导致不同的运营商网关不通，需要针对性的做出判断。

配置
- 注意这俩的metric一定要高，否则会走默认网关
- 不通的ip WAN口设备一定要对应起来。
```
ip route append 10.1.1.1 via 100.69.255.254 dev br-WAN1 proto static src 100.69.211.72 metric 1

ip route append 10.1.1.1 via 100.64.255.254 dev wlan0 proto static src 100.64.249.177 metric 2
```







一个小技巧

**ping指令带上参数就可以指定源ip去ping目的ip。**

```
形式如下：ping -I 192.168.195.130 192.168.195.132
```

