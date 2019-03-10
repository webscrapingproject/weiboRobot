# coding=utf-8
import re
import sys
sys.path.append("..")
from settings import weather_folder,weather_url,img_path,get_one_page
from saveImage import save_image
from pyquery import PyQuery as pq

def weatherCast():
    """
    爬取天气预报
    发送微博
    """
    content=pq(get_one_page(weather_url))
    para= content('.pageContent')
    #print("para",para)
    ## 编辑整理文字信息
    strinfo = re.compile('\n图[0-9].*?\n')
    final=strinfo.sub('\n',para.text())
    ## str还可以抢救一下
    text=final.replace('\n\n','\n')
    ## 最后一张图片没用
    pic=para("a[href]").items()
    #print("pic",pic)
    picList=[]
    for i in pic:
        #print(pic[i].get_attribute("href"))
        url=i.attr("href")
        name=re.sub(r'.*/', '', url).replace('.jpg','')
        save_image(weather_folder,url,name)
        picList.append('{0}/{1}.{2}'.format(img_path + weather_folder, name, 'jpg'))
    ## 去除最后一张图片
    picList.pop()
  ## 返回文字以及下载的图片地址列表
    return(text,picList)


if __name__ == '__main__':
    print(weatherCast())