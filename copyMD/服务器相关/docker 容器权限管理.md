# docker 容器权限管理

先创建一个linux的demo

```
docker run -v $PWD/data:/data  -d --name ubuntu1 ubuntu sleep 10000000
```

加入最后的sleep是为了防止文件直接退出了

挂载后的文件，和宿主机具有同一套文件权限管理系统。也就是说，**在宿主机上的用户权限管理，在容器里面也是认可的。**





## 例子

宿主机：kenger.txt文件在files（1004）用户组里面

![image-20221020134533324](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/b86805c6c426c736260790d05d39a6a1/a684d4d376d178669156fe0fdd10ae96.png)

如果直接在容器里面建立一个用户，进行增删改查，是没有权限的。例如我这里的test用户。

![image-20221020134644235](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/b86805c6c426c736260790d05d39a6a1/f705f064ab72570a50ae80aae723786e.png)



但是如果我将test用户加入到容器李同gid的files用户组里面

![image-20221020134731387](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/b86805c6c426c736260790d05d39a6a1/f57afcc27ca419f27e4e71568cecec9b.png)

那就是有权限的，和宿主机共享一套。

完美实现了权限的管理。



当然很多容器的默认用户是root。可以在一定程度实现越权。这个就看怎么操作了。