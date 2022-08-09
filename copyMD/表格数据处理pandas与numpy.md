# pandas




## 行列
```
# 获取某一列
data['key']

# 获取多列
data[['key1', 'key2']]


```


## 数据条件筛选

**通过[]进行基本的行筛选**

```
# 筛选出key属性等于1的所有行，也可以用>,< 以及用&等逻辑组合
data[data['key'] == 1]

# 筛选出前100行
data[0:100]
```

**通过loc以及iloc进行行以及列的筛选**

- loc按标签值（列名和行索引取值）访问，
- iloc按数字索引访问

**首先loc**

```
# 基本[]支持的loc也都支持
data.loc[data['key'] == 1]

# 同时还支持列的筛选, 列用：同样可以视作全选
data.loc[0:100, ['key1', 'key2']]
```
**然后iloc**

```
# 筛选出前100行，前1,2列
data.iloc[0:100, [0,1]]
```



**关于字符串匹配value**

```
# 下面利用titanic的数据举例，筛选出人名中包含Mrs或者Lily的数据，|或逻辑符号在引号内。
train.loc[train['Name'].str.contains('Mrs|Lily'),:].head()
```

- case=True：使用case指定区分大小写
- **na=True：就表示把有NAN的转换为布尔值True**
- flags=re.IGNORECASE：标志传递到re模块，例如re.IGNORECASE
- regex=True：regex ：如果为True，则假定第一个字符串是正则表达式，否则还是字符串



## 逐行进行遍历

```
# values 是负责把值取出来
for row in CRAN_data.iterrows():
    print(row[1].values)
```




## 查看某一列的特征：平均值，count统计，max，min，std方差

```
data_projects["Platform"].value_counts()
data_projects["Platform"].min()
# 以及mean(), max(),
```
**dataF.describe()**可以一次性查看表的各项属性的特征





# numpy

## 关于reshape

快速改变向量的shape。但是并不会改变原始的顺序。

**也就说说，如果按照从里到外的遍历顺序，那么无论怎么reshape的顺序是不会变的。**

初期数据及库准备：

import numpy as np  # 调用numpy库
# 设置一个1-18的列表
```
anchors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
#将anchors由列表转换为数组的形式
anchors = np.array(anchors)

一维reshape() 为 二维
18个元素一维度数组，可以转换为2 x 9 及 3 X 6的二维数组

print(anchors.reshape([3,6]))  # 生成一个（3，6）的二维数组

print(anchors.reshape([2,9]))  # 生成一个（2，9）的二维数组
```

![3，6的输出结果](https://img-blog.csdnimg.cn/2cfa7cac1afe4bd99e92ac3da0358cf1.png#pic_center)


![](https://img-blog.csdnimg.cn/374c35d44a6148d680b82b630b9d4a06.png#pic_center)


