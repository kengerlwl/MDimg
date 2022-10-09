# logging

通过使用日志模块重载print函数，既保留print的输出，同时又实现logging



```
import logging
import builtins

lr = 0.001
weight_decay=0.001

log_name ="log/"+'{}, lr is {}, weight_decay is {}.log'.format(Platform_name, lr, weight_decay)

# 先情清空文件内容
import os
file = open(log_name,'w');
file = open(log_name, 'w').close()


import datetime
now = datetime.datetime.now()


logger = logging.getLogger()
logger.handlers = []
# print(logger.handlers)

# 如果已经有handler了，那么不用新增新的
if not logger.handlers:
    
    
    # 日志输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # Setup file handler
    fhandler = logging.FileHandler(log_name)
    fhandler.setLevel(logging.INFO)
    fhandler.setFormatter(formatter)

    logger.addHandler(fhandler)
    logger.setLevel(logging.INFO)


# 重载print函数到输出为日志
def print(msg):
#     builtins.print(logger.handlers)
    logger.info('\n{}'.format(msg))
    # 使用系统自带的print函数
    builtins.print(msg)


# 输出一些参数数据
print(graph)
print(logger.handlers)

```

