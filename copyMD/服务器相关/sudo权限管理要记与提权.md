# sudoers文件进行权限管理

作用：能够进行用户以及用户组的权限管理。

使用说明：

**注意，后面的空格只能空一个**

```
# 用户进行权限管理
root    ALL=(ALL) ALL
root表示被授权的用户，这里是根用户；
第一个ALL表示所有计算机；
第二个ALL表示所有用户；
第三个ALL表示所有命令；

# 加入%变成root组。
%root    ALL=(ALL) ALL

# smith组所有用户可以免密码sudo执行useradd，userdel命令
%smith  ALL=(ALL)  NOPASSWD:useradd,userdel
```



## 使用visudo命令进行sudoers文件的修改

如果直接用vim进行sudoers文件的修改，那么是没有纠错功能的，如果sudoers文件配置错误，就会导致用不了sudo权限了，用不了sudo就改不回来了，逻辑闭环。

所以实用visudo命令进行sudoers文件修改，有自动纠错的功能。

进入etc文件夹，输入

```
visudo
```



# 一个遭遇的小问题

**如果在非root用户情况下，sudoers错误情况下用root权限执行命令**

找到一个神奇的方法：远程的话开两个ssh终端，**两个终端要同一个用户**

![img](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/256a8173241b71a641a53b2611818473/d3937500028f3c23bb88cf2d30177105.png)

 对tty1终端：`输入 echo $$` //获取pid

![img](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/256a8173241b71a641a53b2611818473/8023102ce6f8366254f1184377084c9e.png)

切换到tty2：输入 `pkttyagent --process 获取的pid值 ；此时该tty2终端会卡住`

![img](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/256a8173241b71a641a53b2611818473/35c4611902ca88caa0a631c4e84d6769.png)

切到tty1：输入 `pkexec visudo ；此时tty1也会卡住`

![img](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/256a8173241b71a641a53b2611818473/e7d7d494ae4cc05619a8d73e2043aee1.png)

切到tty2：会看到要求输入密码，对应输入

![img](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/256a8173241b71a641a53b2611818473/c7103736a1a11c107746bd6f74137ad4.png)

切回到tty1：发现已经进入了visudo编辑界面，实际上把**pkexec**后面的命令换成其他也是一样的用sudo执行

# ref

[文献1](https://www.cnblogs.com/wayneliu007/p/10321542.html)

