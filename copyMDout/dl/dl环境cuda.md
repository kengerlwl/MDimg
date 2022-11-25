## cuda环境的配置

分为不同的系统，把环境变量的搞好就行





## cuda版本可以向下兼容

比如我的cuda是11.0.

如果我安装需要cuda11.1的库，那么肯定过不了。

但是如果我安装cuda版本为10.1的，那么可以继续兼容安装





## 基于docker 的nvida环境配置

要配置好这个环境1，需要首先安装好NVIDIA Container Toolkit的这个容器。
和配置cuda类似，主要需要注意cuda的版本要和自己的cuda版本兼容

```
# install NVIDIA Container Toolkit

distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
   
curl -s -L https://nvidia.github.io/nvidia-container-runtime/experimental/$distribution/nvidia-container-runtime.list | sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list

sudo apt-get update

sudo apt-get install -y nvidia-docker2

sudo systemctl restart docker


# run a container with gpu

# 一个基于Ubuntu的基础镜像
sudo docker run --rm --gpus all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi


#sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
#or 
#nvidia-docker run --rm all nvidia/cuda:11.0-base nvidia-smi

```





**其他项目如果需要使用到NVIDIA环境，那么需要在启动时声明。**








## mindspore 环境的安装

我这里选择的是用docker去安装



```bash
docker run -i -p 51020:22 -p 51180:8888 -v /dev/shm:/dev/shm -v $PWD/ms:/home --runtime=nvidia swr.cn-south-1.myhuaweicloud.com/mindspore/mindspore-gpu-cuda10.1:1.8.1 
```







## docker ssh服务



设置root用户密码为admin

```
passwd
```



开启容器的ssh服务

https://www.cnblogs.com/devilmaycry812839668/p/13691236.html



```
# update source
apt-get update

# install ssh
apt-get install openssh-server

# maybe need 
mkdir /run/sshd

# start
/usr/sbin/sshd -D &


# 注意

ssh服务，可以设置为该环境的初始启动命令

```



打开root用户的登录权限

```
通过 cat 等指令查看 /etc/ssh/sshd_config 中是否包含类似如下配置：
PermitRootLogin no
改为yes
```

然后重启ssh服务就行





## ref

https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker

https://juejin.cn/post/6999883472487596062