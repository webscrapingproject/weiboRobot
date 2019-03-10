# coding=utf-8
# 国家地理每日一图

import re
import sys
sys.path.append("..")
from settings import geo_folder,geo_url, img_path, get_one_page
from saveImage import save_image
from pyquery import PyQuery as pq


def geogra():
    ## 起始页面
    content = pq(get_one_page(geo_url))
    new_url = content('body > div.content.js_content > div.sec_oneimg.cf > a.con').attr('href')
    #print("para", new_url)
    img_url=content('body > div.content.js_content > div.sec_oneimg.cf > img').attr('src')
    ## 新的页面
    content=pq(get_one_page(new_url))
    text=content('body > div.content.js_content > div.sec_content.cf > div.sec_content_l > div.article_con').text()
    image_name = re.sub(r'.*/', '', img_url).replace('.jpg','')
    ## 保存壁纸
    save_image(geo_folder,img_url,image_name)
    picList=[]
    url='{0}/{1}{2}'.format(img_path+geo_folder, image_name,'.jpg')
    picList.append(url)
    ## 最后一张图片没用

    ## 返回文字以及下载的图片地址列表
    return (text, picList)


if __name__ == '__main__':
    print(geogra())
