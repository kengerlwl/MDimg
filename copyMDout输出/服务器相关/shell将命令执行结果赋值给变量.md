# 语法



shell中将命令结果赋值给变量

两种方法，推荐使用后者，支持嵌套，下面两个参考链接写得很清楚了

```
var=`command`

var=$(command)

```



# demo

一个经典的判断执行结果的例子

```
git_ans='dat8987e'
grep_ans=$(echo $git_ans | grep date)
if [[  $grep_ans != "" ]]
then
  echo $git_ans
else
  echo "仓库文件更新，开始同步"
fi
```



# ref

参考：

http://stackoverflow.com/questions/9449778/what-is-the-benefit-of-using-instead-of-backticks-in-shell-scripts







