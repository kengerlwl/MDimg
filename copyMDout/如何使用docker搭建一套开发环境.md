# 如何使用docker搭建一套开发环境



在群晖，树莓派openwrt等设备上。由于系统以及设备版本等原因。其上面要么不能安装python，java等环境，要么就是安装了也会很多库用不了。总之就是很麻烦。

如果直接安装在docker，在docker里面当服务器重头开始搞一套开发以及部署环境。那又会非常的耗费资源。

因此，为什么不用docker的Ubuntu等当开发环境呢。

**计划：**

- 安装一个Ubuntu的docker容器。
- 在容器内安装python环境。
- 做好目录挂载以及端口开放。（注意容器内的环境只能用容器内的文件项目）
- 通过docker的exec命令执行容器内的脚本以及环境。
- 通过alias别名来设置环境变量。
- 最终就是要运行代码的路径最好和容器内部一致，并且挂载上，这样就能在容器内和容器外都一致了。





## 关于/etc/profile更改环境变量以及别名alias

```
alias ubash='docker exec -it ubuntu2 bash'  # 直接用内部的bash来执行, 不过这招不好使
alias pip='docker exec -it ubuntu2 pip'
alias python='docker exec -it ubuntu2 python3'
```



### 前置配置文件

**/etc/profile：** 此文件为系统的每个用户设置环境信息,当用户第一次登录时,该文件被执行。是系统全局针对终端环境的设置，它是login时最先被系统加载的，是它**调用了/etc/bashrc，以及/etc/profile.d目录下的*.sh文件**，如果有一个软件包，系统上只安装一份，供所有开发者使用，**建议在/etc/profile.d下创建一个新的xxx.sh，配置环境变量。**
**~/.bashrc:**是用户相关的终端（shell）的环境设置，通常打开一个新终端时，默认会load里面的设置，在这里的设置不影响其它人。如果一个服务器多个开发者使用，大家都需要有自己的sdk安装和设置，那么最好就是设置它。





**为了实现内部运行脚本的功能：**

- 要么直接搞个sh文件，然后执行这个sh脚本

- 要么用，（python，一行多命令可以用；）

  ```
   python -c "import os; os.system('cd /volume1/208/csu_tool/Healthy-Punch-Card && python3 auto.py ')"
  ```

  ```
   python -c "import os; os.system('cd /volume1/208/csu_tool/csu_net_keep && python3 main.py')"
  ```

  







## docker部署

**如何给已经运行中的容器挂载新的目录  ,提交现有容器为新镜像，然后重新运行它**

```
$ docker ps  -a
CONTAINER ID        IMAGE                 COMMAND                  CREATED              STATUS                          PORTS               NAMES
   5a3422adeead        ubuntu:14.04          "/bin/bash"              About a minute ago   Exited (0) About a minute ago                       agitated_newton
$ docker commit 5a3422adeead newimagename
$ docker run -ti -v "$PWD/dir1":/dir1 -v "$PWD/dir2":/dir2 newimagename /bin/bash
docker run -d -p 51022:22 -p 8888:8888 --name ubuntu3 -v $PWD/data:/data -v /volume1:/volume1 ubuntu:v3

```





## ubutun容器安装软件

sshd开放。

宝塔面板安装（可以实现很多有用的任务）



## 注意

有些系统里面哪怕是同样安装Ubuntu。但是其会自动吧镜像最小化，导致系统有些功能用不了或者被阉割。

可以用`unminimize`命令来恢复。



