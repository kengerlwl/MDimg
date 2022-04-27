# 关于如何将 MD 的图片换源成github


# 加一个哈希算法
避免图片名字重复


## 首先，去github新建仓库
![](https://raw.githubusercontent.com/2892211452/MDimg/master/image/i.imgur.comVXFAdJ6.png)
## 新建python文件以及需要进行换源的文档
![](https://raw.githubusercontent.com/2892211452/MDimg/master/image/i.imgur.combfKFukZ.png)
py文件代码如下：

注意，要对该文件得一些变量进行配置，
比如:
- 仓库名字地址
- md文档名字
- 还有是否需要代理


```
import  re
import os

#当前文件目录路径
FileDir = os.path.abspath(os.path.dirname(__file__))



# 这里是我的代理， 如果不需要代理删除这个就行， 
proxies = {"http":"http://127.0.0.1:7890", "https":"http://127.0.0.1:7890"}  #设置http和https 代理


os.makedirs( FileDir +'/image/', exist_ok=True)
os.makedirs(FileDir +'/copyMD/', exist_ok=True)

img_dir = FileDir +'/image/'

githubUrl = 'https://github.com/2892211452/MDimg' 
githubUrl = githubUrl + '/blob/master'

name = 'test.md'


def request_download(path,IMAGE_URL):
    import requests
    r = requests.get(IMAGE_URL, proxies = proxies)  #使用代理   ！！！！！！！ 也可以不用，我是境外的网站所以要用
    with open(path, 'wb') as f:
        f.write(r.content)



with open(FileDir+'/' + name, 'r', encoding= 'utf-8', errors='ignore') as  f:
    lines = f.readlines()


mdFile = open( FileDir +'/copyMD/' + name,'w',encoding= 'utf-8',)

for i in lines:
    ans = re.findall(r'!.?((.*?))', i)
    if ans !=[]:
        # print(ans)
        tmp = i.split('(')[1]
        tmp = tmp.replace(')', '')
        tmp = tmp.replace('\n', '')
        name = tmp .replace('https://', '')
        name = name .replace('http://', '')
        name = name .replace('/', '')
        name = name .replace('\n', '')
        path = img_dir + name
        request_download(path,tmp)
        print(tmp , '已经保存到本地')
        url = path.replace(FileDir, '')
        url = githubUrl + url
        print(url)
        i = i.replace(tmp, url)
        print(i)
    mdFile.write(i)


```


## 运行该文件

main.py

查看运行后的md
![](https://raw.githubusercontent.com/2892211452/MDimg/master/image/i.imgur.comIQZHsl3.png)
可以发现，已经换成github了

## 然后将github push上去

![](https://raw.githubusercontent.com/2892211452/MDimg/master/image/i.imgur.comD0PsiaM.png)

## 查看生成的文档：
![](https://raw.githubusercontent.com/2892211452/MDimg/master/image/i.imgur.comtZD4RXW.png)
成功


# 项目地址
[github项目地址](https://github.com/2892211452/MDimg)

有个问题，github的资源更新比较慢。
