from main_单个文件处理 import *
import os

"""
对一个文件夹内部的多个md文件进行批处理换源
"""


# 文件夹路径
dr_Path = './sourcemd'
files =[]
for i,j,k in os.walk(dr_Path):
    # print(i,j,k)
    files.extend(k)
print(files)

# 逐个对文件进行换源操作
for i in files:

    conf['md_name'] = i
    print(i)
    init()
    main()