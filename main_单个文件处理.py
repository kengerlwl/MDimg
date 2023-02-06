import re
import os
import 加密算法.mymd5 as md5
import requests
from PIL import Image
from Config import *

# 这里是我的代理， 如果不需要代理删除这个就行，
proxies = {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"}  # 设置http和https 代理

# 转换后的图片url前缀
github_url = None
md_name = None
md_name_hash = None
content = None
md_file = None
img_dir_pre = None  # 图片存储的目录
conf = get_config()

# 文件夹路径
out_path = 'copyMDout输出'

def request_download(path, IMAGE_URL):
    """
    :param path: 被存储到的路径
    :param IMAGE_URL: 图片的url
    :return:
    """
    if conf['proxy']:
        r = requests.get(IMAGE_URL, proxies=proxies)  # 使用代理   ！！！！！！！ 也可以不用，我是境外的网站所以要用
    else:
        r = requests.get(IMAGE_URL)
    with open(path, 'wb') as f:
        f.write(r.content)


def init():
    global github_url
    global md_name
    global content
    global md_file
    global img_dir_pre
    global md_name_hash

    github_url = 'https://github.com/' + conf['username'] + '/' + conf['repository']
    github_url = github_url.replace('https://github.com/', '')
    github_url = 'https://raw.githubusercontent.com/' + github_url
    github_url = github_url + '/master'
    print('github image url 的链接前缀 ： ' + github_url)

    md_name = conf['md_name']
    md_name_hash = md5.my_md5(md_name)
    img_dir_pre = FileDir + '/image/' + md_name_hash + '/'

    # 新建可能需要的目录
    os.makedirs(FileDir + '/image/', exist_ok=True)
    os.makedirs(FileDir + '/'+out_path+'/', exist_ok=True)
    os.makedirs(FileDir + '/image/' + md_name_hash, exist_ok=True)

    # 打开待处理文件夹
    with open(conf['complete_name'], 'r', encoding='utf-8', errors='ignore') as f:
        content = f.readlines()

    md_file = open(conf['complete_name'], 'w', encoding='utf-8', )


def img_pro(img_url):
    global github_url
    global md_name
    global content
    global md_file
    global img_dir_pre
    global md_name_hash
    new_local_img_path = img_dir_pre + md5.my_md5(img_url) +'.png'
    new_github_img_path = github_url + '/image/' + md_name_hash +'/' + md5.my_md5(img_url) +'.png'
    # http 图片
    if re.findall('http', img_url) != []:
        request_download(new_local_img_path , img_url)

    # 本地的图片
    else:
        img = Image.open(img_url)
        img.save(new_local_img_path, 'png')

    return new_github_img_path


def main():
    global github_url
    global md_name
    global content
    global md_file
    global img_dir_pre

    for line in content:
        image_urls = re.findall(r'!\[.*\]\((.*)\)', line)  # 检验有没有图片,并提取出来
        # print(image_urls)
        if image_urls != []:
            # print(image_urls)
            try:
                image_url = image_urls[0]
                print(image_url)
                if image_url.find("raw.githubusercontent.com") != -1:
                    # print(image_url.find("raw.githubusercontent.com"))
                    raise Exception("已经是github图源了")

                git_url = img_pro(image_url)
                print(git_url)
                line = line.replace(image_url, git_url)
            except Exception as e:
                print(e)
                pass
        else:
            pass
        md_file.write(line)


if __name__ == '__main__':

    conf['md_name'] = "README.md"
    conf['complete_name'] = "./README.md"
    init()
    main()
