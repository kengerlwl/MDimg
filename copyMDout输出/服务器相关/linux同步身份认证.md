# ldap 在linux上同步身份认证

# 安装ldap及其管理器环境

[参考compose文件](https://github.com/2892211452/docker_demo/tree/main/ldap_compose)

安装完成后，可以看到管理界面
![](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/4ecf958df4cd734532cd81636478dda9/5fef2c31edb928d7b2c1b99c6e422b78.png)


具体如何进行账号添加，小组管理可以翻阅相关文档。这里不作展开。


# 在linux上配置nslcd连接ldap
首先要安装相关库
```
yum install nss-pam-ldapd
```

**如果不确定本地是否能够连通服务器ldap，可以用ldap的客户端进行连通性测试**
`yum install nss-pam-ldapd openldap-clients openldap -y`

**测试ldap服务连通性**
```
ldapsearch -x -H ldap://110.40.*.*:389 -b dc=lwl,dc=com -D "cn=admin,dc=lwl,dc=com" -w your_password
```



**注，如果是Ubuntu，那么直接安装**

```
apt-get install libnss-ldapd libpam-ldapd 
```





## linux本地配置相关文件

`vi /etc/nsswitch.conf`

关键是在这三组后面添加ldap

```
passwd:     files sss ldap
shadow:     files sss ldap
group:      files sss ldap
```

修改`/etc/nslcd.conf` 文件

```
# The user and group nslcd should run as.
uid nslcd
gid ldap


uri ldap://110.40.*.*



base dc=lwl,dc=com
binddn cn=admin,dc=lwl,dc=com
bindpw your_password
ssl no
tls_cacertdir /etc/openldap/cacertsorg
```



修改`/etc/openldap/ldap.conf`文件

```
TLS_CACERTDIR /etc/openldap/cacerts

# Turning this off breaks GSSAPI used with krb5 when rdns = false

SASL_NOCANON    on
URI ldap://110.40.*.*/
BASE dc=lwl,dc=com
```

为了解决新建用户后没有home目录的问题。
```
# 在su的时候新建home目录。配置vi /etc/pam.d/system-auth 新增一行配置
session required pam_mkhomedir.so skel=/etc/skel umask=0022

# 在ssh的时候新建home目录， 在/etc/pam.d/sshd后面新增一行
session    required     pam_mkhomedir.so 
```

**配置完后，启动相关程序**
```
systemctl restart nslcd
systemctl restart sshd
```

## 配置自动同步authconfig，不然密码认证可能不过

安装`yum install authconfig`

运行：
```
authconfig --enableldap --enableldapauth --ldapserver="110.40.*.*" --ldapbasedn="dc=lwl,dc=com" --update
```



# 最后getent查看数据库

我们要查看目前有多少用户或者用户组需要用getent命令这个命令可以查看当前的所有信息。包括在线的ldap的数据库里面的用户。
`getent passwd`

![](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/4ecf958df4cd734532cd81636478dda9/d440b86a9717540789e1a35b5c1c366f.png)



# 解决一些后序问题

- 解决一些后序问题

    - ssh连接用户home目录没有的问题
    - 管理用户权限管理的问题。 例如要执行docker命令，但是普通用户没有权限。

    **solution：**

    写一个脚本去监听所有用户，如果当前用户没有home目录，就新建。然后针对每个用户，在.bashrc文件里面对sudo进行alias别名封装一部分docker命令。

    **bashrc_demo文件**

    ```
    
    # 封装docker命令
    alias docker="sudo /usr/bin/docker"
    ```

    **bash_profle_demo文件**

    因为如果仅仅新建.bashrc 文件，那么ssh进去以后并不会一定执行，加入该文件能够ssh后自动执行bashrc文件。

    ```
    # if running bash  
    if [ -n "$BASH_VERSION" ]; then  
        # include .bashrc if it exists  
        if [ -f "$HOME/.bashrc" ]; then  
            . "$HOME/.bashrc"  
        fi  
    fi 
    ```

    **shell 脚本**

    - 检查所有用户目录是否创建，没有就建立
    - 检查所有用户的.bashrc等配置文件是否创建
      - 没有就创建demo
      - 有的话就比对我们需要缝合进去的命令，如果缺少就加入（这样可以当个人修改了一些自己需要的bashrc配置后，可以继续在上一个人的基础上添加公共配置）

    ```
    #!/usr/bin/bash
    while(true)
    do
        # 睡一秒
        sleep 1
        
        # 如果后序匹配特征变了，可以适当改变grep的匹配规则
        home_drs=$(getent passwd  | grep /home | awk -F: '{print$6}')
        #echo $home_drs
        for home_dr in $home_drs;
        do
    
            #echo $home_dr
    
            #判断用户文件夹是否存在
            if [ ! -d "$home_dr" ]; then
              mkdir $home_dr
              echo "创建文件夹" $home_dr
            fi
    
    
            #判断bash_profile配置文件是否存在
            file_pre="$home_dr/.bash_profile"
            if [ ! -f "$file_pre" ];
             then
              cp bash_profile_demo "$file_pre"
              echo "创建文件" "$file_pre"
            fi
    
            #判断bashrc配置文件是否存在
            file="$home_dr/.bashrc"
            #file=/home/liuwenlong/.bashrc
            if [ ! -f "$file" ];
             then
              cp bashrc_demo "$file"
              echo "创建文件" $file
             else
              echo 'file存在'
              # 选择去除空行和注释后的命令，判断是否需要加入
              cat bashrc_demo | grep -v '#' | grep -v '^$' | while read line
              do
                        #echo $line
    
                        # 判断匹配函数，匹配函数不为0，则包含给定字符
                        if [ ! `grep -c "$line" $file` -ne '0' ];
                        then
                            echo "没有命令行 $line ,补上 "
                            echo "$line" >> $file
    
                        fi
              done
    
            fi
             
        done
    
    
    done
    ```

    **sudoers文件**

    ```
    # ldap组执行权限开放 docker 命令
    %group1  ALL=(ALL)      NOPASSWD:/usr/bin/docker
    ```

    # ref

    [OpenLDAP同步linux用户](https://blog.csdn.net/weixin_42728895/article/details/114540168) [linux nslcd服务,](https://blog.csdn.net/weixin_42101056/article/details/116740544?spm=1001.2101.3001.6650.5&utm_medium=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~default-5-116740544-blog-116740538.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~default-5-116740544-blog-116740538.pc_relevant_default&utm_relevant_index=10)

    [CentOS 6通过ldap集成AD域账号(nslcd方式)](https://blog.csdn.net/weixin_42101056/article/details/116740544?spm=1001.2101.3001.6650.5&utm_medium=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~default-5-116740544-blog-116740538.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~default-5-116740544-blog-116740538.pc_relevant_default&utm_relevant_index=10)

    [配置Linux使用LDAP用户认证的方法](https://cloud.tencent.com/developer/article/1721854?from=15425)
- ](https://cloud.tencent.com/developer/article/1721854?from=15425)
