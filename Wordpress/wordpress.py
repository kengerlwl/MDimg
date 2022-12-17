# coding:utf-8
import os  # 用来遍历文件路径
import sys
from Config import *
# 1 导入frontmatter模块
import frontmatter

# 2 导入markdown模块
import markdown

# 3 导入wordpress_xmlrpc模块
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.methods.posts import GetPosts, EditPost



def make_post(filepath, metadata):
    """
    make a WordPressPost for Client call
    :param filepath: 要发布的文件路径
    :param metadata: 字典类型
             包括 metadata['category']: 文章分类
                  metadata['tag']: 文章标签
                  metadata['status']: 有publish发布、draft草稿、private隐私状态可选
    :return WordPressPost: if success
            None: if failure
    """
    filename = os.path.basename(filepath)  # 例如：test(2021.11.19).md
    filename_suffix = filename.split('.')[-1]  # 例如：md
    filename_prefix = filename.replace('.' + filename_suffix, '')  # 例如：test(2021.11.19)；注意：这种替换方法要求文件名中只有一个".md"

    # 目前只支持 .md 后缀的文件
    if filename_suffix != 'md':
        return None

    # 1 通过frontmatter.load函数加载读取文档里的信息，包括元数据
    post_from_file = frontmatter.load(filepath)

    # 2 markdown库导入内容
    post_content_html = markdown.markdown(post_from_file.content, extensions=['markdown.extensions.fenced_code'])
    post_content_html = post_content_html.encode("utf-8")

    # 3 将本地post的元数据暂存到metadata中
    metadata['title'] = filename_prefix  # 将文件名去掉.md后缀，作为标题
    # metadata['slug'] = metadata['title']  # 别名
    metadata_keys = metadata.keys()
    # 如果post_from_file.metadata中的属性key存在，那么就将metadata[key]替换为它
    for key in metadata_keys:
        if key in post_from_file.metadata:  # 若md文件中没有元数据'category'，则无法调用post.metadata['category']
            metadata[key] = post_from_file.metadata[key]

    # 4 将metadata中的属性赋值给post的对应属性
    post = WordPressPost()  # 要返回的post
    post.content = post_content_html
    post.title = metadata['title']
    # post.slug = metadata['slug']
    post.post_status = metadata['status']
    post.terms_names = {
        'category': metadata['category'],
        'post_tag': metadata['tag']
    }
    post.comment_status = 'open'  # 开启评论
    return post


def push_post(post, client):
    """
    上传post到WordPress网站
    :param post: 要发布的文章（WordPressPost类型），由make_post函数得到
    :param client: 客户端
    :return True: if success
    """
    return client.call(NewPost(post))


def get_filepaths(path):
    """
    如果path是目录路径，递归遍历path目录下的所有文件，将所有文件路径存入filepaths
    如果path是文件路径，直接将单个文件路径存入filepaths
    :param path: 你要上传的目录路径或文件路径（绝对路径）
    :return filepaths: 该目录下的所有子文件或单个文件的绝对路径
            None: wrong path
    """
    filepaths = []
    if os.path.isdir(path):  # 当前路径是目录
        for now_dirpath, child_dirnames, child_filenames in os.walk(path):
            for filename in child_filenames:
                filepath = os.path.join(now_dirpath, filename)
                filepaths.append(filepath)
        return filepaths
    elif os.path.isfile(path):  # 当前路径是文件
        return [path]
    else:  # wrong path
        return None




def find_post(filepath, client):
    """
    find the post in WordPress by using filename in filepath as the searching title
    :param filepath: 更新用的文件路径
    :param client: 客户端
    :return True: if success
    """
    filename = os.path.basename(filepath)  # 例如：test(2021.11.19).md
    filename_suffix = filename.split('.')[-1]  # 例如：md
    filename_prefix = filename.replace('.' + filename_suffix, '')  # 例如：test(2021.11.19)；注意：这种替换方法要求文件名中只有一个".md"
    # 目前只支持 .md 后缀的文件
    if filename_suffix != 'md':
        print('ERROR: not Markdown file')
        return None
    # get pages in batches of 20
    offset = 0  # 每个batch的初始下标位置
    batch = 20  # 每次得到batch个post，存入posts中
    while True:  # 会得到所有文章，包括private(私密)、draft(草稿)状态的
        posts = client.call(GetPosts({'number': batch, 'offset': offset}))
        if len(posts) == 0:
            return None  # no more posts returned
        for post in posts:
            title = post.title
            if title == filename_prefix: # 这里是根据标题名字来选择的
                return post
        offset = offset + batch


def update_post_content(post, filepath, client):
    """
    update a post in WordPress with the content in file path
    :param post: 已发布的文章（WordPressPost类型），由find_post函数得到
    :param filepath: 更新用的文件路径
    :param client: 客户端
    :return True: if success
    """
    post_from_file = frontmatter.load(filepath)  # 读取文档里的信息
    post_content_html = markdown.markdown(post_from_file.content,
                                          extensions=['markdown.extensions.fenced_code']).encode("utf-8")  # 转换为html
    post.content = post_content_html  # 修改内容
    return client.call(EditPost(post.id, post))


class WordpressUploader():
    def __init__(self):
        # User Configuration
        conf  = get_config()
        domain = conf['wordpress']['host']  # e.g. https://jwblog.xyz（配置了SSL证书就用https，否则用http）
        username = conf['wordpress']['username']
        password = conf['wordpress']['password']


        # Optional Configuration
        self.post_metadata = {
            'category': [],  # 文章分类
            'tag': ["bot_publish"],
            'status': 'publish'  # 可选publish发布、draft草稿、private隐私状态
        }

        self.client = Client(domain + '/xmlrpc.php', username, password)  # 客户端


    # 如果同名文章不存在，就上传，如果存在，就更新
    def upload_and_update(self, path):
        filepaths = get_filepaths(path)
        if filepaths is None:
            print('FAILURE: wrong path')
            sys.exit(1)
        md_cnt = 0
        all_cnt = len(filepaths)
        process_number = 0
        failpaths = []  # 存储上传失败的文件路径
        for filepath in filepaths:
            # 先清空
            self.post_metadata['category'] = []
            # 根据文件目录获取分类
            category = filepath.split('/')
            if len(category)>2:
                category = category[-2]
            else:
                category = "综合"
            self.post_metadata['category'].append(category)


            process_number = process_number + 1

            post = find_post(filepath, self.client)
            # 如果已经存在了，update
            if post is not None:
                self.update(filepath)
                md_cnt = md_cnt + 1
            else:
                post = make_post(filepath, self.post_metadata)
                filename = os.path.basename(filepath)



                if post is not None:
                    push_post(post, self.client)
                    md_cnt = md_cnt + 1
                    print('Process number: %d/%d  SUCCESS: Push "%s" completed!' % (process_number, all_cnt, filename))
                else:
                    failpaths.append(filepath)
                    print('Process number: %d/%d  WARNING: Can\'t push "%s" because it\'s not Markdown file.' % (
                        process_number, all_cnt, filename))
        print('-----------------------------------------------END-----------------------------------------------')
        print('SUCCESS: %d files have been pushed to your WordPress.' % md_cnt)

        if len(failpaths) > 0:
            print('WARNING: %d files haven\'t been pushed to your WordPress.' % len(failpaths))
            print('\nFailure to push these file paths:')
            for failpath in failpaths:
                print(failpath)



    # 这里只能是文件的path
    def update(self, filepath):
        post = find_post(filepath, self.client)
        if post is not None:
            ret = update_post_content(post, filepath, self.client)
            if ret:
                print('SUCCESS to update the file: "%s"' % filepath)
            else:
                print('FAILURE to update the file: "%s"' % filepath)
        else:
            print('FAILURE to find the post. Please check your User Configuration and the title in your WordPress.')


if __name__ == '__main__':
    path = 'copyMD'  # e.g. D:/PythonCode/post-wordpress-with-markdown/doc
    WP = WordpressUploader()
    WP.upload_and_update(path)