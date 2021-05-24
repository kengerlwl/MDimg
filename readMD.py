import  re
import os
import 加密算法.mymd5 as md5
import requests
from PIL import Image


#当前文件目录路径
FileDir = os.path.abspath(os.path.dirname(__file__))


# 这里是我的代理， 如果不需要代理删除这个就行， 
proxies = {"http":"http://127.0.0.1:7890", "https":"http://127.0.0.1:7890"}  #设置http和https 代理


os.makedirs( FileDir +'/image/', exist_ok=True)
os.makedirs(FileDir +'/copyMD/', exist_ok=True)

img_dir = FileDir +'/image/'

githubUrl = 'https://github.com/2892211452/MDimg' 
githubUrl = githubUrl.replace('https://github.com/', '')
githubUrl = 'https://raw.githubusercontent.com/' + githubUrl
githubUrl = githubUrl + '/master'
print('github 的链接 ： '+githubUrl)

MDname = '数字图像处理.md'


def request_download(path,IMAGE_URL):
    r = requests.get(IMAGE_URL, proxies = proxies)  #使用代理   ！！！！！！！ 也可以不用，我是境外的网站所以要用
    with open(path, 'wb') as f:
        f.write(r.content)



with open(FileDir+'/' + MDname, 'r', encoding= 'utf-8', errors='ignore') as  f:
    lines = f.readlines()


mdFile = open( FileDir +'/copyMD/' + MDname,'w',encoding= 'utf-8',)

for i in lines:
    try:
        ans = re.findall(r'!.?((htt.*?))', i) # 检验有没有https图片
        ans2 = re.findall(r'C:\\.*',i) # 检验有没有本地图片
        if ans !=[]:
            # print(ans)

            tmp = i.split('(')[1]
            tmp = tmp.replace(')', '')
            tmp = tmp.replace('\n', '')
            name = tmp .replace('https://', '')
            name = name .replace('http://', '')
            name = name .replace('/', '')
            name = name .replace('\n', '')
            path = img_dir + md5.my_md5(name) +'.png'
            request_download(path,tmp)
            print(tmp , '已经保存到本地')
            # print(path, 'path')
            url = path.replace(FileDir, '')
            # print(url)
            url = githubUrl + url
            print('图片在github上的链接 ： '+url)
            i = i.replace(tmp, url)
        elif ans2 != []:
            tmp = i.split('(')[1]
            tmp = tmp.replace(')', '')
            tmp = tmp.replace('\n', '')
            path = img_dir + md5.my_md5(tmp) + '.png'
            print(tmp)
            img = Image.open(tmp)
            img.save(path, 'png')

            url = path.replace(FileDir, '')
            url = githubUrl + url
            print('图片在github上的链接 ： ' + url)
            i = i.replace(tmp, url)





        mdFile.write(i)
    except Exception as e:
        mdFile.write(i)
        print(e)



