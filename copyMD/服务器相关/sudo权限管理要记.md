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

![img](https://img2018.cnblogs.com/blog/701047/201901/701047-20190125235320075-118033541.png)

 对tty1终端：`输入 echo $$` //获取pid

![img](https://img2018.cnblogs.com/blog/701047/201901/701047-20190125235407460-1863815435.png)

切换到tty2：输入 `pkttyagent --process 获取的pid值 ；此时该tty2终端会卡住`

![img](https://img2018.cnblogs.com/blog/701047/201901/701047-20190125235513643-118611276.png)

切到tty1：输入 `pkexec visudo ；此时tty1也会卡住`

![img](https://img2018.cnblogs.com/blog/701047/201901/701047-20190125235620485-657232856.png)

切到tty2：会看到要求输入密码，对应输入

![img](https://img2018.cnblogs.com/blog/701047/201901/701047-20190125235719530-1480569268.png)

切回到tty1：发现已经进入了visudo编辑界面，实际上把**pkexec**后面的命令换成其他也是一样的用sudo执行

# ref

[文献1](https://www.cnblogs.com/wayneliu007/p/10321542.html)

