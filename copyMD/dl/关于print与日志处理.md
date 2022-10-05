# logging

通过使用日志模块重载print函数，既保留print的输出，同时又实现logging



```
import logging
import builtins

log_name ='{}.log'.format('my')
logger = logging.getLogger()
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
    logger.info('p{}'.format(msg))
    # 使用系统自带的print函数
    builtins.print(msg)

print('kjhkajshdf')
```

