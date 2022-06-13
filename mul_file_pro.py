from main import *

import os
filePath = './sourcemd'
files =[]
for i,j,k in os.walk(filePath):
    # print(i,j,k)
    files.extend(k)
print(files)

# 逐个对文件进行换源操作
for i in files:

    conf['md_name'] = i
    print(i)
    init()
    main()