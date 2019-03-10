# coding=utf-8
import os
import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import *
from selenium.common.exceptions import TimeoutException
from random import randint

class weibo_robot():
    def __init__(self):
        self.weiboUrl = weibo_url
        self.weatherUrl = weather_url
        self.imgFolder=img_folder
        self.imgPath=img_path
        self.options=chrome_options
        self.browser = webdriver.Chrome(options=self.options)
        self.wait = WebDriverWait(self.browser, 20)

       
    def __del__(self):
        self.browser.quit()  
    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot     
    
    def login(self,email,password):
        """
        登录微博
        """
        self.browser.get(self.weiboUrl)
        name = self.wait.until(EC.element_to_be_clickable((By.ID, 'loginName')))
        pwd = self.wait.until(EC.element_to_be_clickable((By.ID, 'loginPassword')))
        name.send_keys(email)
        pwd.send_keys(password)
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'loginAction')))
        submit.click()
        time.sleep(3)
       # self.browser.execute_script("window.open();")
        #time.sleep(3)
# switch to the new window which is second in window_handles array
       # self.browser.switch_to.window(self.browser.window_handles[1])
        #self.browser.get('https://weibo.com')
        #print('登录成功')
    def jump(self):
        time.sleep(3)
        self.browser.execute_script("window.open();")
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.get('https://weibo.com')
    def login_successfully(self):
        """
        判断是否登录成功
        :return:
        """
        try:
            return bool(
                WebDriverWait(self.browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'lite-iconf-profile'))))
        except TimeoutException:
            return False
    def crack(self):
        """
        输入文字
        """
        captcha=self.browser.find_element_by_class_name('embed-captcha')
        loc=self.browser.find_element_by_class_name('i_top')
        action = ActionChains(self.browser)
        action.move_to_element(loc).perform()
        for i in range(10):
            time.sleep(0.5)
            #print("success")
            x=randint(0, 20)
            y=randint(0, 20)
            #print(x,y)
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=y).perform()
        #action.click()
        action.move_to_element(captcha).perform()
        time.sleep(1)
        action.click().perform()
        time.sleep(2)
        #ActionChains(self.browser).click_and_hold(captcha).perform()
    def upload_txt(self,text):
        """
        输入文字
        """
        #newpost = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'lite-iconf-releas')))
        #newpost.click()
        input_w = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea[title="微博输入框"]')))
        input_w.send_keys(text)
    def upload_pic(self,url):
        """
        上传图片
        """
        input_w = self.browser.find_element_by_css_selector('input[name="pic1"]')
        input_w.send_keys(url.decode("utf-8"));
        time.sleep(5)
    def send(self):
        """
        找到发布按钮并点击
        """
        send=self.browser.find_element(By.CSS_SELECTOR, 'a[title="发布微博按钮"]')
        js="var elements = document.getElementsByClassName('m-mask');while(elements.length > 0){elements[0].parentNode.removeChild(elements[0]);}"
        self.browser.execute_script(js)
        send.click()
    def newPost(self,text,picList):
        self.upload_txt(text)
        ## 一条微博最多上传9张图片
        if len(picList)<9:
            size=picList
        else:   
            ## 取前9个
            size=picList[0:9]
        for i in size:
            self.upload_pic(i)
            os.remove(i)
            print(i)
        #time.sleep(3)
        self.send()
        time.sleep(3)
        #print('successful post')
