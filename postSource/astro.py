# coding=utf-8
# 北京天文馆每日一图

import re
import sys

sys.path.append("..")
from settings import astro_folder, astro_url, img_path, get_one_page
from saveImage import save_image
from pyquery import PyQuery as pq


def astro():
    ## 起始页面
    content = pq(get_one_page(astro_url))
    new_url = 'http://www.bjp.org.cn/'+content('b > a').attr('href')
    #print("para", new_url)
    ## 新的页面
    content=pq(get_one_page(new_url))
    img_url='http://www.bjp.org.cn/'+content('img').attr('src')
    text=content('.juzhong').text()
    image_name = re.sub(r'.*/', '', img_url).replace('.jpg','')
    ## 保存壁纸
    save_image(astro_folder,img_url,image_name)
    picList=[]
    url='{0}/{1}{2}'.format(img_path+astro_folder, image_name,'.jpg')
    picList.append(url)
    ## 最后一张图片没用

    ## 返回文字以及下载的图片地址列表
    return (text, picList)


if __name__ == '__main__':
    print(astro())
