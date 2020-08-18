import  re
import os
from path import *

proxies = {"http":"http://127.0.0.1:7890", "https":"http://127.0.0.1:7890"}  #设置http和https 代理


os.makedirs( FileDir +'/image/', exist_ok=True)
os.makedirs(FileDir +'/copyMD/', exist_ok=True)

img_dir = FileDir +'/image/'

githubUrl = ''
name = 'test.md'


def request_download(path,IMAGE_URL):
    import requests
    r = requests.get(IMAGE_URL, proxies = proxies)  #使用代理
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
        i = i.replace(tmp, path)
        print(i)
    mdFile.write(i)



