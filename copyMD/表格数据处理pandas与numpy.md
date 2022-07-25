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

