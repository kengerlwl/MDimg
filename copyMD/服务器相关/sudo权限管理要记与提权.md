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

![img](https://raw.githubusercontent.com/2892211452/MDimg/master/image/e09b44733b8bab72990d5e40b3bcb69c/e3e8639dd831b735642e605ccc98633b.png)

 对tty1终端：`输入 echo $$` //获取pid

![img](https://raw.githubusercontent.com/2892211452/MDimg/master/image/e09b44733b8bab72990d5e40b3bcb69c/8553a5cf738f52d6744883d14c9294e6.png)

切换到tty2：输入 `pkttyagent --process 获取的pid值 ；此时该tty2终端会卡住`

![img](https://raw.githubusercontent.com/2892211452/MDimg/master/image/e09b44733b8bab72990d5e40b3bcb69c/7a63cd8c0ae43c4b884b7b0a372bd21b.png)

切到tty1：输入 `pkexec visudo ；此时tty1也会卡住`

![img](https://raw.githubusercontent.com/2892211452/MDimg/master/image/e09b44733b8bab72990d5e40b3bcb69c/2e87ef8581039357afd440a5f9df053d.png)

切到tty2：会看到要求输入密码，对应输入

![img](https://raw.githubusercontent.com/2892211452/MDimg/master/image/e09b44733b8bab72990d5e40b3bcb69c/5e9ad097ba63376251f15cd919447a52.png)

切回到tty1：发现已经进入了visudo编辑界面，实际上把**pkexec**后面的命令换成其他也是一样的用sudo执行

# ref

[文献1](https://www.cnblogs.com/wayneliu007/p/10321542.html)

