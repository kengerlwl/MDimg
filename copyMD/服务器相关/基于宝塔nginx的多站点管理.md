# 应用的场景

有若干服务需要访问，他们或者ip不一样，或者端口不一样。

如果一个个的去绑定隐形url域名挺麻烦的。也没必要。

一个优秀的办法是，通过不同的域名访问过去。然后根据域名不同做反向代理。



# demo

我服务器上有一个wordpress，其端口是8081。我想要通过`blog.kenger.com`去访问该服务。



## 设置二级域名

先直接将域名指向服务器ip。或者服务器www域名也可以。总之就是直接到80端口。

![image-20221217203603861](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/7d3fdd730213faafd876f5c39adc98ca/f6fdfb6c69c5f7b513aa171974e0ea87.png)

## 设置宝塔面板nginx

然后去宝塔

![image-20221217203731037](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/7d3fdd730213faafd876f5c39adc98ca/efcab459a012bf898b8bc6260ddaf6a8.png)



添加一个站点

![image-20221217203751574](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/7d3fdd730213faafd876f5c39adc98ca/ea3a5a87ac083d069d4d82b89c69c386.png)



设置反向代理到本地

![image-20221217204302535](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/7d3fdd730213faafd876f5c39adc98ca/693152a0e565faee0ca878b3661da118.png)

### 错误注意

尽量不要用localhost。用127.0.0.1更好。

![image-20221217203808588](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/7d3fdd730213faafd876f5c39adc98ca/b403b7242a1e21d95530d7cce95128dc.png)



然后就可以访问了



![image-20221217204312605](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/7d3fdd730213faafd876f5c39adc98ca/860676fa93d310175d980bf6a266df6d.png)





