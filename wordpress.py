from Wordpress import *


if __name__ == '__main__':
    path = 'copyMD'  # e.g. D:/PythonCode/post-wordpress-with-markdown/doc
    WP = WordpressUploader()
    WP.upload_and_update(path)