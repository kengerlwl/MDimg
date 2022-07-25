# 协程，进程，线程概念

- 进程：资源占用的基本单位。
- 线程：执行任务的单位，一个进程可以有多个线程。

**以上两者，如果要实现并发，那么利用的是多核cpu的并行能力。**但是协程不一样，协程实际上还是单线程

- 协程：**程序员通过高超的代码能力，在代码执行流程中人为的实现多任务并发，是单个线程内的任务调度技巧。**



# python的协程------yield，next，send

```
def simple_coroutine():
    print('-> 启动协程')
    y = 10
    
    # 遇到yield就暂停返回，直到next再返回过来，
"""
    var = yield xxxx的赋值形式。它同时具备两个功能，一是暂停并返回函数，二是接收外部send()方法发送过来的值，重新激活函数，并将这个值赋值给var变量！
"""
    x = yield y
    print('-> 协程接收到了x的值:', x)

my_coro = simple_coroutine()
ret = next(my_coro)
print(ret)
my_coro.send(10)
```



# python协程------async，await

```
import asyncio
import datetime

async def display_date(num, loop):      # 注意这一行的写法
    end_time = loop.time() + 10.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(2)  # 阻塞直到协程sleep(2)返回结果

loop = asyncio.get_event_loop()  # 获取一个event_loop
tasks = [display_date(1, loop), display_date(2, loop)]
loop.run_until_complete(asyncio.gather(*tasks))  # "阻塞"直到所有的tasks完成
loop.close()

```


- 创建事件循环
- 指定循环模式并运行
- 关闭循环



# 一个spider的样例
```
import asyncio
import aiohttp
import time

start = time.time()

async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    await response.text()
    await session.close()
    return response

async def request():
    url = 'https://httpbin.org/delay/5'
    print('Waiting for', url)
    response = await get(url)
    print('Get response from', url, 'response', response)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)
```
