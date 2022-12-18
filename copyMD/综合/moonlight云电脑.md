# 场景

有一台配置有N卡的win，有一个可能不在同一个局域网的PC机B。

想要让主机B能够流畅的控制桌面使用win。

使用moonlight



# 具体

**我走的服务器代理，所以延迟会比较高**，50ms

### win上配置Nvidia Geforce Experience的Shield

你需要安装Nvidia Geforce Experience，在它的设置中找到并启用Shield串流服务。这个需要比较彻底的科学上网才能开，建议

- 使用openwrt
- 使用clash的![image-20221218215126294](https://raw.githubusercontent.com/2892211452/MDimg/master/image/73e9ab486fd11539c76112ad3b7a06ee/71c4e16c76dc63cec19feefff7a71af5.png)



开启

![image-20221218215224220](https://raw.githubusercontent.com/2892211452/MDimg/master/image/73e9ab486fd11539c76112ad3b7a06ee/4bd9e731a11798c1480b4119a1ec0b5d.png)



一个用来重启`NvContainerLocalSystem`的bat脚本

```
@echo off
echo 关闭服务
net stop "NvContainerLocalSystem"
timeout 2
echo 开启服务
net start "NvContainerLocalSystem"
```





### 在win上配置frp客户端代理到服务器公网

如果要代理到公网，就用这个

配置文件为`frpc.ini`，修改其内容如下：

```
[common]
server_addr = <Your server IP>
server_port = <Your selected port>
token = <Your password>

[nvidia-stream-tcp-1]
type = tcp
local_ip = 127.0.0.1
local_port = 47984
remote_port = 47984

[nvidia-stream-tcp-2]
type = tcp
local_ip = 127.0.0.1
local_port = 47989
remote_port = 47989

[nvidia-stream-tcp-3]
type = tcp
local_ip = 127.0.0.1
local_port = 48010
remote_port = 48010

[nvidia-stream-udp-1]
type = udp
local_ip = 127.0.0.1
local_port = 5353
remote_port = 5353

[nvidia-stream-udp-2]
type = udp
local_ip = 127.0.0.1
local_port = 47998
remote_port = 47998

[nvidia-stream-udp-3]
type = udp
local_ip = 127.0.0.1
local_port = 47999
remote_port = 47999

[nvidia-stream-udp-4]
type = udp
local_ip = 127.0.0.1
local_port = 48000
remote_port = 48000

[nvidia-stream-udp-5]
type = udp
local_ip = 127.0.0.1
local_port = 48002
remote_port = 48002

[nvidia-stream-udp-6]
type = udp
local_ip = 127.0.0.1
local_port = 48010
remote_port = 48010
```





### 如何使用moonlight连接

输入ip就可以了

![image-20221218215436510](https://raw.githubusercontent.com/2892211452/MDimg/master/image/73e9ab486fd11539c76112ad3b7a06ee/468699ab353a98c772a03dd2fa79f380.png)