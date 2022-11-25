# python 错误处理

## try and except捕获异常
可以通过用多个except捕获多个异常
```
try:
    print 2/'0'
except ZeroDivisionError:
    print '除数不能为0'
except Exception:
    print '其他类型异常'
except Exception as e: # 捕获到错误本体
    print(e)
```

## final句子,最终必执行
finally子句和try子句联合使用但是和except语句不同，finally不管try子句内部是否有异常发生，都会执行finally子句内的代码。所有一般情况下，finally自己常常用于关闭文件或者在Socket中。

```
try:
    print 2/'0'
except (ZeroDivisionError,Exception):
    print '发生了一个异常'
finally:
    print '不管是否发生异常都执行'
```

## raise抛出一个异常

```
def ThorwErr():
    raise Exception("抛出一个异常") 
# Exception: 抛出一个异常 
ThorwErr()
```