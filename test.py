s = '![1-0bc2d58fee7642019cb30bd7a602e575](Caksjdfkjsd)'

import re

ans = re.findall(r'!\[.*\]\((.*)\)', s)  # 检验有没有https图片,并提取出来
print(ans)
print(s.split('(')[1])