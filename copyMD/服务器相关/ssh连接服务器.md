# 常见连接服务器方式

## 密码

输入密码连接，符合直觉高效。

缺点：不安全，尤其是一些弱密码



## 秘钥登录服务器

生成秘钥

```
ssh-keygen
```

![image-20230113162239303](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/691a708e850e02dce427debbb2f5a7fe/b7ea389ea57bcd57b016567deeb9676e.png)

将公钥添加到服务器的某个账户上，然后在客户端利用私钥即可完成认证并登录。这样一来，没有私钥，任何人都无法通过 SSH 暴力破解你的密码来远程登录到系统

其中

id_rsa：是访问本地端的私钥

id_rsa.pub：是放在服务器端的公钥





### 设置 SSH，打开密钥登录功能

将公钥放入服务器

**直接将id_rsa.pub里面的东西复制到另一台的$USER/.ssh/authorized_keys里面**





编辑 /etc/ssh/sshd_config 文件，进行如下设置：

```
RSAAuthentication yes
PubkeyAuthentication yes
```

另外，请留意 root 用户能否通过 SSH 登录：

```
PermitRootLogin yes
```

当你完成全部设置，并以密钥方式登录成功后，再禁用密码登录：(可以同时开启秘钥登录和密码登录)

```
PasswordAuthentication no
```

最后，重启 SSH 服务：

```
service sshd restart
```





## vscode配置本地秘钥登录

```
Host gpu2.csubot.cn
  HostName gpu2.csubot.cn
  User liuwenlong
  IdentityFile /Users/lwl/.ssh/id_rsa
```

