# python 请求重试机制tenacity

优秀的参考
 [ref](https://www.cnblogs.com/wuzhibinsuib/p/13443622.html)
`from tenacity import *`



# 正常看到错误就重试
```
@retry
def test_retry1():
    print("等待重试.....")
    raise Exception  # 通过raise直接返回一个错误
```


# 设置最大的重试次数
```
@retry(stop=stop_after_attempt(5))
def test_retry2():
    print("等待重试.....")
    raise Exception
```

# 设置最大重试时间， 这里的意思是5秒内如果还错误就继续执行
```
@retry(stop=stop_after_delay(5))
def test_retry3():
    print("等待重试.....")
    return "hello" + 1
```

# 指定特定的错误类型

```
@retry(retry=retry_if_exception_type(TypeError))
def test_retry4():
    print("等待重试.....")
    raise TypeError # 捕获类型错误，当出现类型错误时重试
```


# 同时设置多个参数
```
from tenacity import retry, stop_after_delay, stop_after_attempt

@retry(stop=(stop_after_delay(5) | stop_after_attempt(7)))
def test_retry():
    print("等待重试....")
    raise Exception

test_retry()

```

# 自定义
```


# 首先定义了一个函数symbol，它的作用是判断传入的值是否为None；它返回一个布尔值，如果结果value=None，则返回true，否则返回False
def symbol(value):
    return value is None


# 装饰器中retry=retry_if_result(symbol)，表示把test_retry函数的结果传入symbol，判断test_retry的结果是否为None，
# 如果=None，就进行重试(retry),如果不等于None，就结束并返回函数值（所以达成重试的条件是test_retry的结果是否为条件函数定义的结果）
@retry(stop=stop_after_attempt(3), retry=retry_if_result(symbol), reraise=True)
def test_retry():
    print("等待重试.....")
    return None

if __name__ == '__main__':
    test_retry5()
````