# coding=utf-8
import re
import sys
sys.path.append("..")
from saveImage import *

def bingWallpaper():

    img=requests.get(img_url).json()
    ## 得到壁纸图片地址
    pic_url=base_url+img['images'][0].get('url')
    ## 得到文字
    text=img['images'][0].get('copyright')
    ## 设置壁纸图片名称
    image_name = re.sub(r'.*/', '', pic_url).replace('.jpg','')
    ## 保存壁纸
    save_image(bing_folder,pic_url,image_name)
    ## 上传图片
    picList=[]
    url='{0}/{1}{2}'.format(img_path+bing_folder, image_name,'.jpg')
    picList.append(url)
    return(text,picList)

if __name__ == '__main__':
    print(bingWallpaper())