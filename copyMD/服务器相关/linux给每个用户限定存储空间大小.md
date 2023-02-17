## 前置测试工具

**随机生成一定大小的文件**

```
out_file_name=out.txt
#生成一个1G 的文件，内容全部为0
dd if=/dev/zero of=out_file_name bs=1M count=1000

#生产一个1G 的文件，内容随机
dd if=/dev/urandom of=out_file_name bs=1M count=1000
```







## 磁盘配额工具(Quota)

### 限制

- 针对整个 partition（分区）：
  quota 实际在运作的时候，是针对『整个 partition』进行限制的， 例如：如果你的 /dev/hda5 是挂载在 /home 底下，那么在 /home 底下的所有目录都会受到限制！
- 只对一般身份使用者有效：
  这就有趣了！并不是所有在 Linux 上面的账号都可以设定 quota 呢，例如 **root 就不能设定 quota** ， 因为整个系统所有的数据几乎都是他的！



### 一些配置说明

quota 这支程序针对整个 partition 的限制项目主要分为底下几个部分：

- soft：
  这是最**低限制容量**的意思，用户在宽限期间之内，他的容量可以超过 soft ，但必需要宽限时间之内将磁盘容量降低到 soft 的容量限制之下！
- hard：
  **这是『绝对不能超过』的容量**！跟 soft 相比的意思为何呢？通常 hard limit 会比 soft limit 为高，例如网络驱动器空间为 30 MB ，那么 hard limit 就设定为 30MB ，但是为了让使用者有一定的警戒心，所以当使用空间超过 25 MB 时，例如使用者使用了 27 MB 的空间时，那么系统就会警告用户， 让使用者可以在『宽限时间内』将他的档案量降低至 25 MB ( 亦即是 soft limit )之内！也就是说， soft 到 hard 之间的容量其实就是宽限的容量啦！可以达到针对使用者的『警示』作用！
- 宽限时间：
  那么宽限时间就可以很清楚的知道含意是什么了！也就是当您的使用者使用的空间超过了 soft limit ，却还没有到达 hard limit 时，那么在这个『宽限时间』之内， 就必需要请用户将使用的磁盘容量降低到 soft limit 之下！而当用户将磁盘容量使用情况超过 soft limit 时，『宽限时间』就会自动被启动，而在用户将容量降低到 soft limit 之下，那么宽限时间就会自动的取消啰！





## quota实操

### 流程

 Quota 从开始准备 filesystem 的支持到整个设定结束的主要的步骤大概是：

1. **设定 partition 的 filesystem 支持 quota 参数：**
   由于 quota 必须要让 partition 上面的 filesystem 支持才行，一般来说， 支持度最好的是 ext2/ext3 ，其他的 filesystem 类型鸟哥我是没有试过啦！ 启动 filesystem 支持 quota 最简单就是编辑 /etc/fstab ，使得准备要开放的 quota 磁盘可以支持 quota 啰；
2. **建立 quota 记录文件：**
   刚刚前面讲过，整个 quota 进行磁盘限制值记录的档案是 aquota.user/aquota.group， 要建立这两个档案就必须要先利用 quotacheck 扫瞄才行喔！所以啰，接下来的步骤就是： 使用 quotacheck 来扫瞄一下我们要使用的磁盘啰；
3. **编辑 quota 限制值数据：**
   再来就是使用 edquota 来编辑每个使用者或群组的可使用空间啰；
4. **重新扫瞄与启动 quota ：**
   设定好 quota 之后，建议可以再进行一次 quotacheck ，然后再以 quotaon 来启动吧！

### 1 建立测试环境

新建好用户和分组

```
[root@linux ~]# groupadd qgroup
[root@linux ~]# useradd -m -g qgroup quser1
[root@linux ~]# useradd -m -g qgroup quser2
[root@linux ~]# passwd quser1
[root@linux ~]# passwd quser2
```



### **2 建立好 filesystem 的 quota 支持：**

查看系统的文件挂载情况

```
[root@linux ~]# df -h
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/hda1              5952252   3193292   2451720  57% /
/dev/hdb1             28267608     77904  26730604   1% /disk2  # 这是我们计划挂载的点，/disk2
/dev/hda5              9492644    227252   8775412   3% /disk1
```

编辑 `/etc/fstab`文件，在指定目录下面加入,usrquota,grpquota（**在  defaults,usrquota,grpquota  之间都没有空格！）**

```
[root@linux ~]# vi /etc/fstab
LABEL=/        /          ext3    defaults                    1 1
LABEL=/disk1   /disk1     ext3    defaults                    1 2
LABEL=/disk2   /disk2     ext3    defaults,usrquota,grpquota  1 2 # 这里是更改的地方
/dev/hda3      swap       swap    defaults                    0 0
```

**由于真正的 quota 在读取的时候是读取 /etc/mtab 这个档案的，偏偏这一个档案需要重新启动之后才能够以 /etc/fstab 的新数据进行改写！**

**Solution:**

```
# 1重启
reboot

# 2重新挂载
[root@linux ~]# mount -o remount /disk2
```



### **3 扫瞄磁盘的用户使用状况，并产生重要的 aquota.group 与 aquota.user：文件**

用到`quotacheck`生成配置文件

```
[root@linux ~]# quotacheck -avug   # 生成配置文件
quotacheck: Scanning /dev/hdb1 [/disk2] done
quotacheck: Checked 3 directories and 4 files
[root@linux ~]# ll /disk2          # 查看
-rw-------  1 root root  6144 Sep  6 11:44 aquota.group
-rw-------  1 root root  6144 Sep  6 11:44 aquota.user
```



### 4 **启动 quota 的限额：**

```
[root@linux ~]# quotaon -avug
/dev/hdb1 [/disk2]: group quotas turned on
/dev/hdb1 [/disk2]: user quotas turned on
```



### 5 **编辑使用者的可使用空间：**

主要分为针对用户还是分组进行限制

- 用户：设置每单个用户的限额
- 分组：设置某个小组所有用户加起来的限制



**实操**

使用`edquota`设置用户`quser1` 的限额

```
[root@linux ~]# edquota -u quser1   # 输入该命令，会弹出一个vim的编辑框。修改配置即可
Disk quotas for user quser1 (uid 502):
  Filesystem    blocks    soft    hard   inodes   soft   hard
  /dev/hdb1          0   45000   50000        0      0      0

# 说明
soft的单位是KBytes。要转化为MB请除以1024
```

设置用户的限制时间（这个是针对整个分区设置的，所有用户都会一致）

```
edquota -t
```



将某个用户的限制粘贴给另一个用户（**如果quser2已经有配置了，那么会覆盖掉原有配置**）

```
[root@linux ~]# edquota -p quser1 quser2  # 把quser1的复制给 quser2
```





**查看各用户配置以及使用情况**

**1**

```
[root@linux ~]# quota [-uvsl] [username]
[root@linux ~]# quota [-gvsl] [groupname]
参数：
-u  ：后面可以接 username ，表示显示出该用户的 quota 限制值。若不接 username 
      ，表示显示出执行者的 quota 限制值。
-g  ：后面可接 groupname ，表示显示出该群组的 quota 限制值。
-v  ：显示每个 filesystem 的 quota 值；
-s  ：可选择以 inode 或磁盘容量的限制值来显示；
-l  ：仅显示出目前本机上面的 filesystem 的 quota 值。
范例：

范例一：秀出目前 root 自己的 quota 限制值：
[root@linux ~]# quota -guvs

范例二：秀出 quser1 这个用户的磁盘配额
[root@linux ~]# quota -u quser1
# 注意一下这两个范例，如果您的系统上面尚未有任何的 quota 支持的 filesystem 时，
# 使用这两个范例时，『不会有任何信息列出来』啦！不要以为发生错误啰！
```

**或者2**

```
repquota -a
```





### 6 **设定开机时启动 quota**

```
[root@linux ~]# vi /etc/rc.d/rc.local 在里面加入一行 (直接加在最后一行即可)：如下
/sbin/quotaon -avug
```





## 一个针对某个小组每个人设置限额的脚本

思路：

- 设置一个模板用户：example（对该用户设置想要的限额）
- 针对某用户组所有的用户，将example的配置复制过去。
  - 考虑到有用户更新，那么就分两个接口
  - 1，强制复制，所有人原有的配置都重新更改为example
  - 2，只针对目前没有限制的人做复制



```


```





## ref

[鸟哥linux](http://cn.linux.vbird.org/linux_basic/fedora_4/0420quota-fc4.php)
