s = '![1-0bc2d58fee7642019cb30bd7a602e575](https://www.zabbx.cn/upload/2021/02/1-0bc2d58fee7642019cb30bd7a602e575.png)'

import re

ans = re.findall(r'!.*(htt.*?)', s)  # 检验有没有https图片
print(ans)