# coding=utf-8
from settings import *
import os
import requests

def save_image(folder,url,name):
    """
    下载图片并保存
    """
    if not os.path.exists(img_folder):
        os.mkdir(img_folder)
    if not os.path.exists(folder):
        os.mkdir(folder)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(folder, name, 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')

if __name__ == '__main__':
    save_image(img_folder,'http://s.cn.bing.net/th?id=OJ.dl7bFq17Wv69Dg&pid=MSNJVFeeds','test')