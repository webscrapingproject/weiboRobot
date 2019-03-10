# coding=utf-8
from selenium.webdriver.chrome.options import Options
import os
import requests
# 微博登录界面
weibo_url='https://passport.weibo.cn/signin/login'

# 图片下载
img_path=os.getcwd()+'/'
# 图片文件夹
img_folder='img'

# 天气预报相关参数
# 每日天气
weather_url='http://www.weather.com.cn/index/zxqxgg1/new_wlstyb.shtml'
weather_folder='img/weather'

# bing壁纸相关
# bing 故事
base_url = 'http://cn.bing.com/'
img_url='https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
# 壁纸保存位置
bing_folder='img/bing'


# 天文相关
astro_url='http://www.bjp.org.cn/col/col89/index.html'
astro_folder='img/astro'

# 国家地理
geo_url='http://www.ngchina.com.cn/index.php'
geo_folder='img/geo'



chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--start-maximized') #指定浏览器分辨率
chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
#chrome_options.add_argument('--hide-scrollbars')
#chrome_options.add_argument('blink-settings=imagesEnabled=false')
def get_one_page(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
    response = requests.get(url,headers=headers)
    response.encoding = "utf-8"
    if response.status_code == 200:
        return response.text
    return None