## /dev 目录

/dev这个目录对所有的用户都十分重要。因为在这个目录中包含了所有Linux系统中使用的外部设备。但是这里并不是放的外部设备的驱动程序，这一点和windows,dos操作系统不一样。它实际上是一个访问这些外部设备的端口。我们可以非常方便地去访问这些外部设备，和访问一个文件，一个目录没有任何区别。
**Linux沿袭[Unix](http://www.ltesting.net/html/76/category-catid-376.html)的风格，将所有设备认成是一个文件。**

一些常见的设备：

```
　　/dev/hd[a-t]：IDE设备

　　/dev/sd[a-z]：SCSI设备

　　/dev/fd[0-7]：标准软驱

　　/dev/md[0-31]：软raid设备

　　/dev/loop[0-7]：本地回环设备

　　/dev/ram[0-15]：内存

　　/dev/null：无限数据接收设备,相当于黑洞

```

