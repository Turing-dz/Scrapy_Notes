import scrapy
from selenium import webdriver#pip install selenium
from mouse import move,click #pip install mouse
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pickle
from selenium.webdriver import ChromeOptions
import os
from urllib import request
from pyppeteer import launch
import asyncio
import random
import cv2
import pickle

import random
# from ArticleSpider.selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from urllib import parse
import os
project_dir="C:/Users/dz/Desktop/ArticleSpider/ArticleSpider"
def get_dis(bg, fg):
    img = cv2.imread(bg)
    temp = cv2.imread(fg)
    res = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)[3][0]  # 滑块需要滑行的距离
    # 如果网页展示对图片有压缩 那滑动距离也需要等比例压缩
    dis = value * 1
    print("********************")
    print(cv2.minMaxLoc(res))
    print("********************")
    return dis
from PIL import Image

def crop_transparent_background(image_path, output_path, size=(60, 60)):
    # 打开图片
    img = Image.open(image_path)
    
    # 将图片转换为 RGBA 模式以处理透明背景
    img = img.convert("RGBA")
    
    # 创建一个新的图像，大小与原图像相同
    new_img = Image.new("RGBA", size, (255, 255, 255, 0))  # 使用透明背景
    
    # 计算裁剪区域
    left = (img.width - size[0]) / 2
    top = (img.height - size[1]) / 2
    right = left + size[0]
    bottom = top + size[1]
    
    # 裁剪原图像到指定大小
    img_cropped = img.crop((left, top, right, bottom))
    
    # 将裁剪后的图像粘贴到新图像上
    new_img.paste(img_cropped, (0, 0), img_cropped)
    
    # 保存新图像
    new_img.save(output_path, format="PNG")


   


class ZhihuSpider(scrapy.Spider):
    name="zhihu"
    allowed_domains=["www.zhihu.com"]
    start_urls=['https://www.zhihu.com/']
       
    def start_requests(self):
        cookies=[] 
        #取cookies
        if os.path.exists(project_dir+"/cookies/zhihu.cookie"):
            cookies=pickle.load(open(project_dir+"/cookies/zhihu.cookie","rb"))
        if not cookies:
        # cookies=pickle.load(open("C:/Users/dz/Desktop/ArticleSpider/ArticleSpider/cookies/zhihu.cookie","rb"))#读取cookies
        # cookies_dict={}
        # for cookie in cookies:
        #     cookies_dict[cookie["name"]]=cookie["value"]
        #     print(cookies)
            #1.设置
            option= ChromeOptions()
            option.add_experimental_option("excludeSwitches", ["enable-automation"])
            option.add_experimental_option('useAutomationExtension', False)
            service = Service(executable_path="C:/Program Files/Google/Chrome/Application/chromedriver.exe")
            browser = webdriver.Chrome(service=service, options=option)
            browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })
            """
            })
            browser.execute_cdp_cmd("Network.enable", {})
            browser.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser1"}})
            browser.maximize_window()
            #2.登录
            browser.get("https://www.zhihu.com/signin")
            browser.find_element(By.CSS_SELECTOR,".SignFlow-tab:not(.SignFlow-tab--active)").click()
            browser.find_element(By.CSS_SELECTOR, ".SignFlow-accountInput.Input-wrapper.QZcfWkCJoarhIYxlM_sG input").send_keys(Keys.CONTROL+"a")#全选中
            browser.find_element(By.CSS_SELECTOR, ".SignFlow-accountInput.Input-wrapper.QZcfWkCJoarhIYxlM_sG input").send_keys("18811752638")
            browser.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div/div/div/div[2]/div/div[1]/div/div[1]/form/div[3]/div/label/input').send_keys(Keys.CONTROL+"a")
            browser.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div/div/div/div[2]/div/div[1]/div/div[1]/form/div[3]/div/label/input').send_keys("190023dz") 
            # browser.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div/div/div/div[2]/div/div[1]/div/div[1]/form/div[3]/div/label/input').send_keys(Keys.ENTER)
            time.sleep(3)
            move(1444,727)
            time.sleep(3)
            click()
            # browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/div[2]/div/div[1]/div/div[1]/form/button').submit()
            time.sleep(7)
            #滑动验证码
            #获取两个图片css-6m0nd1
            # login=False
            # while not login:
            #     try:
            #         browser.find_element(By.CLASS_NAME,"Tabs-link AppHeader-TabsLink is-active css-1fb8pjf")
            #         login=True
                    
            #     except NoSuchElementException:
            #         print("找不到 start_create 元素，说明没进入主页")
            #         time.sleep(5)
            #         img_src = browser.find_element(By.CLASS_NAME, "yidun_bg-img").get_attribute('src')
            #         request.urlretrieve (img_src,'image.png')#下载图片
            #         temp_src = browser.find_element(By.CLASS_NAME, "yidun_jigsaw").get_attribute('src')
            #         request.urlretrieve (temp_src,'temp.png')#下载图片
            #         crop_transparent_background('temp.png', 'cropped_temp.png')#裁剪，60*60
            #         dis = get_dis ('image.png','cropped_temp.png') #缺口识别
            #         actions = ActionChains(browser)# 初始化ActionChains对象
            #         slider = browser.find_element(By.CLASS_NAME, "yidun_jigsaw")# 模拟拖动操作，找到滑动条元素
            #         actions.click_and_hold(slider)# 按住滑块
            #         actions.move_by_offset(dis+15, 10)# 模拟滑动一定距离（例如，滑动200像素）
            #         actions.release().perform()# 释放滑块
            #         time.sleep(1)# 让程序等待几秒观察效果
            #         move(1444,727)
            #         click()
            #         time.sleep(5)
            time.sleep(5)
            img_src = browser.find_element(By.CLASS_NAME, "yidun_bg-img").get_attribute('src')
            request.urlretrieve (img_src,'image.png')#下载图片
            temp_src = browser.find_element(By.CLASS_NAME, "yidun_jigsaw").get_attribute('src')
            request.urlretrieve (temp_src,'temp.png')#下载图片
            crop_transparent_background('temp.png', 'cropped_temp.png')#裁剪，60*60
            dis = get_dis ('image.png','cropped_temp.png') #缺口识别
            actions = ActionChains(browser)# 初始化ActionChains对象
            slider = browser.find_element(By.CLASS_NAME, "yidun_jigsaw")# 模拟拖动操作，找到滑动条元素
            actions.click_and_hold(slider)# 按住滑块
            actions.move_by_offset(dis+15, 10)# 模拟滑动一定距离（例如，滑动200像素）
            actions.release().perform()# 释放滑块
            time.sleep(1)# 让程序等待几秒观察效果
            move(1444,727)
            click()
            time.sleep(5)
            
            
            
            
            #存cookies
            cookies=browser.get_cookies()
            pickle.dump(cookies,open(project_dir+"/cookies/zhihu.cookie","wb"))
        cookies_dict={}
        for cookie in cookies:
            cookies_dict[cookie["name"]]=cookie["value"]
            print(cookies)
        for url in self.start_urls:
            yield scrapy.Request(url,dont_filter=True,cookies=cookies_dict)
        
        # #3.获取cookies
        # #(现在settings里面设置COOKIES_ENABLED = True
        # # COOKIES_DEBUG = True
        # # USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        # # DOWNLOADER_MIDDLEWARES = {
        # #    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':2
        # # })
        # browser.get("https://www.zhihu.com/")
        # cookies=browser.get_cookies()
        # pickle.dump(cookies,open("C:/Users/dz/Desktop/ArticleSpider/ArticleSpider/cookies/zhihu.cookie","wb"))#保存到本地
        
        
    def parse(self,response):
        all_urls=response.css("a::attr(href)").extract()
        all_urls=[parse.urljoin(response.url,url) for url in all_urls]
        for url in all_urls:
            print(url)


