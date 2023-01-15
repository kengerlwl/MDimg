# 情况

我正在用transformer训练自己的一个数据集。

结果

![image-20230113225050509](/Users/lwl/Library/Application Support/typora-user-images/image-20230113225050509.png)



显然不对了。loss值变成了nan。



# 排查



## 1，学习率太大，导致溢出了

尝试调低学习率，更改模型初始化参数





## 2，模型本身问题

但是发现我这一开始loss就是nan。

![image-20230113225244523](/Users/lwl/Library/Application Support/typora-user-images/image-20230113225244523.png)

模型内部应该加入SIGMOD之类的防止越界



然后输出模型的的out查看

![image-20230113230413317](/Users/lwl/Library/Application Support/typora-user-images/image-20230113230413317.png)

发现第一次的数据就有nan值。不知道是中间哪一层开始的。



检查开始：

- 检查输入是不是异常含有nan值：pass，这里不是
- 一层层网络检查是从哪一层开始出现nan