# jupyter

为了方便在js里面实现一些例如goto之类的功能。

比如我调参的时候，需要返回到某一行更改参数后重新开始往下执行。

众所周知，python是不支持goto语句的。这里采取类似自动化的方式实现



## js与jupyter

一个显而易见的办法是使用selenium自动化协议个自动执行脚本。但是这样会比较麻烦。

在查阅相关资料后。获悉，jupyter在浏览器里面会有一个jupyter对象。可以通过对这个对象执行函数，实现全部自动化操作。可以在控制台执行。

![image-20221009193043155](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/536c1e5c631aea0dfc3c8ce5d0023b10/a80556c4920ffd60f5aec9fe4ce89f11.png)

下面讲解一些实用的函数。



### 方框是分类种类的。

![image-20221009173853724](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/536c1e5c631aea0dfc3c8ce5d0023b10/fa0fdcf30c916680d10ff5ed3ef4bb7f.png)

图里面，第一个是md框，第二个是代码执行框。



### select选择

第一种，是直接选择第一个框，无论它是什么类型

```
Jupyter.notebook.select(0)
```



### 移动选择光标

选择下一个框

```
Jupyter.notebook.select_next()
```



### 获取当前选择框的index

当然也可以获取其他属性

```
Jupyter.notebook.get_selected_index()
```



### 执行当前选择的框

执行完后并不会自动忘后跳

```
Jupyter.notebook.execute_cell()
```



### 执行所有后面的框

包括当前框，并且会自动跳到末尾

```
Jupyter.notebook.execute_cells_below()
```



### 一个简单的goto demo

````
for(var i=0; i<100; i++){
  Jupyter.notebook.select(15);
  Jupyter.notebook.execute_cells_below();
}

````

