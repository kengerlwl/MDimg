from main_单个文件处理 import *
import os
import shutil
"""
对一个文件夹内部的多个md文件进行批处理换源
"""


# 文件夹路径
dr_Path = './copyMD'



# 对文件夹整体拷贝，是为了实现目录层级,先删后拷贝
shutil.rmtree('./copyMDout')
shutil.copytree(dr_Path, './copyMDout')



# 获取所有待处理文档的路径，这里是打算直接在copy文件夹里面操作，直接覆盖
files =[]
for root, dir,file in os.walk('./copyMDout'):
    for file_name in file:
        # 如果是md文档
        if file_name.endswith('.md'):

            complete_name = root + "/"+ file_name
            files.append([complete_name, file_name])
            print(complete_name)


# 逐个对文件进行换源操作
for complete_name, file_name in files:

    conf['md_name'] = file_name
    conf['complete_name'] = complete_name

    init()
    main()