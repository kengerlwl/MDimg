# 应用的场景

有若干服务需要访问，他们或者ip不一样，或者端口不一样。

如果一个个的去绑定隐形url域名挺麻烦的。也没必要。

一个优秀的办法是，通过不同的域名访问过去。然后根据域名不同做反向代理。



# demo

我服务器上有一个wordpress，其端口是8081。我想要通过`blog.kenger.com`去访问该服务。



## 设置二级域名

先直接将域名指向服务器ip。或者服务器www域名也可以。总之就是直接到80端口。

![image-20221217203603861](https://raw.githubusercontent.com/2892211452/MDimg/master/image/7d3fdd730213faafd876f5c39adc98ca/37c57ef6a84a5c47efe7a06d38397e1b.png)

## 设置宝塔面板nginx

然后去宝塔

![image-20221217203731037](https://raw.githubusercontent.com/2892211452/MDimg/master/image/7d3fdd730213faafd876f5c39adc98ca/87f5c8b0a5c411d8f00163cc0832245b.png)



添加一个站点

![image-20221217203751574](https://raw.githubusercontent.com/2892211452/MDimg/master/image/7d3fdd730213faafd876f5c39adc98ca/5f5223ab4d957d75fe48eb9c468462a7.png)



设置反向代理到本地

![image-20221217204302535](https://raw.githubusercontent.com/2892211452/MDimg/master/image/7d3fdd730213faafd876f5c39adc98ca/91d53881cd3f75902d0a995a3afd3fd2.png)



![image-20221217203808588](https://raw.githubusercontent.com/2892211452/MDimg/master/image/7d3fdd730213faafd876f5c39adc98ca/711d3ca9458779ea6d08dbd5c5cb63c5.png)



然后就可以访问了



![image-20221217204312605](https://raw.githubusercontent.com/2892211452/MDimg/master/image/7d3fdd730213faafd876f5c39adc98ca/a04c3adb65e79bcf6f9ade4810328678.png)





