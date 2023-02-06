# 关于如何将 MD 的图片换源成github



# 使用前编辑配置文件

![image-20230206205436715](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/04c6e90faac2675aa89e2176d2eec7d8/dbb4269a401b961e45b40c12d51bfeeb.png)

```
{
  "username": "kengerlwl", # 用户名
  "repository" : "MDimg", # 仓库名
  "proxy": true, # 针对特殊图片，是否使用代理
  "wordpress": { # 上传到wordpress的配置
    "host": "http://host:8081",
    "username": "***",
    "password": "***"
  }
}
```



# 单文件使用

![image-20230206205223812](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/04c6e90faac2675aa89e2176d2eec7d8/50fe86a639e05acf27a546ab81ac3dbb.png)



- 然后上传仓库。



# 多文件批量更换

**这里设置默认更改这个文件夹的所有文档图源**

![image-20230206205616493](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/04c6e90faac2675aa89e2176d2eec7d8/c9683de0999cae2ce963333b3166135d.png)



## 生成的新图源文档在如下文件夹

![image-20230206205730187](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/04c6e90faac2675aa89e2176d2eec7d8/570b3a5cf2a5c523732de1b349308d3b.png)



