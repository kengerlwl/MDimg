# Samba用户管理

**关于samba用户与系统用户关系**

```
基本没有关系，但是samba可以使用系统用户，只是并不是一套密码
```





**新建系统测试账号**

```
$sudo useradd test  //新建一个名为test的账号
$sudo passwd test   //为test账号设置密码
```

**新增samba账号** 

```
$sudo smbpasswd -a test //以系统账号test为基础建立samba用户test
```



**在vim /etc/config/samba文件末尾添加如下：**     

```
config sambashare 'kenger'  ## 引号中可改为想要的共享名称，建议不要有中文
        option name 'kenger'  ## 引号中可改为想要的共享名称，建议不要有中文，与上面相同
        option path '/mnt/test'  ## 引号中改为U盘挂载位置
        option read_only 'no'
        option guest_ok 'no'
        option create_mask '777'
        option dir_mask '777'
```

编辑配置文件**vim /etc/samba/smb.conf.template **

可以直接复制

```
[global]
	netbios name = |NAME|
	display charset = |CHARSET|
	interfaces = |INTERFACES|
	server string = |DESCRIPTION|
	unix charset = |CHARSET|
	workgroup = |WORKGROUP|
	browseable = yes
	deadtime = 30
	domain master = yes
	encrypt passwords = true
	enable core files = no
	guest account = nobody
	guest ok = yes
	#invalid users = root
	local master = yes
	load printers = no
	map to guest = Bad User
	max protocol = SMB2
	min receivefile size = 8192
	null passwords = yes
	obey pam restrictions = yes
	os level = 20
	passdb backend = smbpasswd
	preferred master = yes
	printable = no
	security = user
	smb encrypt = disabled
	smb passwd file = /etc/samba/smbpasswd
	socket options = TCP_NODELAY SO_RCVBUF=960000 SO_SNDBUF=960000
	syslog = 2
	use sendfile = yes
	use mmap = yes
	writeable = yes
	disable spoolss = yes
	host msdfs = no
	strict allocate = No

```





**进行权限设置** 

```


通过设置test及其目录的访问权限，可达到对不同目录的不同的访问权限。 

修改samba用户的密码 
$sudo smbpasswd 用户名

禁用samba用户 
$sudo smbpasswd -d 用户名

启用samba用户 
$sudo smbpasswd -e 用户名

删除samba用户 
$sudo smbpasswd -x 用户名
```





