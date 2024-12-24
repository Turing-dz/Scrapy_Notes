import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib import parse
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
from PIL import Image
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from urllib import parse
import os
import re
from ArticleSpider.items import LagouJobItem,LagouJobItemLoader
from ArticleSpider.utils.common import get_md5
from datetime import datetime
def get_dis(bg, fg):
    img = cv2.imread(bg)
    temp = cv2.imread(fg)
    res = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)[2][0]  # 滑块需要滑行的距离
    # 如果网页展示对图片有压缩 那滑动距离也需要等比例压缩
    dis = value * 342 / 360
    return dis
project_dir="C:/Users/dz/Desktop/ArticleSpider/ArticleSpider"
def get_dis(bg, fg):
    img = cv2.imread(bg)
    temp = cv2.imread(fg)
    res = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)[2][0]  # 滑块需要滑行的距离
    # 如果网页展示对图片有压缩 那滑动距离也需要等比例压缩
    dis = value * 1
    print("********************")
    print(cv2.minMaxLoc(res))
    print("********************")
    return dis
class LagouSpider(CrawlSpider):
    name = "lagou"
    allowed_domains = ["www.lagou.com"]
    start_urls = ["https://www.lagou.com/wn/"]
    #1.首先selenium登录拿到cookie
    def start_requests(self):
        cookies=[] 
        #取cookies
        if os.path.exists(project_dir+"/cookies/lagou.cookie"):
            cookies=pickle.load(open(project_dir+"/cookies/lagou.cookie","rb"))
        if not cookies:
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
            browser.get("https://www.lagou.com/wn/")
            time.sleep(5)
            browser.find_element(By.CSS_SELECTOR,".login").click()
            time.sleep(5)
            browser.find_element(By.CSS_SELECTOR,".sc-fotOHu.fLmipN > .sc-giYglK.gKjFct > .sc-ezbkAF.bUNcAS").click()##########
            time.sleep(5)
            browser.find_element(By.CSS_SELECTOR, ".sc-fKVqWL.jaxjxQ[type='text']").send_keys("18811752638")
            browser.find_element(By.CSS_SELECTOR, ".sc-fKVqWL.jaxjxQ[type='password']").send_keys("190023Dz!") 
            time.sleep(3)
            browser.find_element(By.CSS_SELECTOR,".sc-furwcr.bVYGWy").click()
            browser.find_element(By.CSS_SELECTOR,".ant-btn.ant-btn-primary").click()
            time.sleep(5)
            
            
            try:
                style_attribute_b = browser.find_element(By.CLASS_NAME, "geetest_bg").get_attribute('style')# 获取 style 属性的值
                img_src = re.search(r'url\("(.*?)"\)', style_attribute_b).group(1)
                request.urlretrieve (img_src,'image.png')#下载图片
                style_attribute_t = browser.find_element(By.CLASS_NAME, "geetest_slice_bg").get_attribute('style')
                temp_src = re.search(r'url\("(.*?)"\)', style_attribute_t).group(1)
                request.urlretrieve (temp_src,'temp.png')#下载图片
                dis = get_dis ('image.png','temp.png') #缺口识别
                actions = ActionChains(browser)# 初始化ActionChains对象
                slider = browser.find_element(By.CLASS_NAME, "geetest_arrow")# 模拟拖动操作，找到滑动条元素
                actions.click_and_hold(slider)# 按住滑块
                actions.move_by_offset(dis+15, 10)# 模拟滑动一定距离（例如，滑动200像素）
                actions.release().perform()# 释放滑块
            except:
                browser.find_element(By.CSS_SELECTOR,".geetest_refresh").click()
                time.sleep(5)
                
            time.sleep(60)
            #存cookies
            cookies=browser.get_cookies()
            pickle.dump(cookies,open(project_dir+"/cookies/lagou.cookie","wb"))
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "Referer": "https://www.lagou.com",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "X-Requested-With": "XMLHttpRequest",
        }
        cookies_dict={}
        for cookie in cookies:
            cookies_dict[cookie["name"]]=cookie["value"]
        print(cookies)
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, dont_filter=True,cookies=cookies_dict)
        
    rules = (
        Rule(LinkExtractor(allow=("zhaopin/.*")),follow=True),
        Rule(LinkExtractor(allow=("gongsi/j\d+.html")),follow=True),
        Rule(LinkExtractor(allow=r"jobs/\d+.html"), callback="parse_item", follow=True))
    # def parse_start_url(self, response, **kwargs):
    #     return []

    # def process_results(self, response: Response, results: list):
    #     return results 
    def parse_item(self, response):
        item = {}
        print("*****************************")
        print(response.url)
        print("*****************************")
        
        item_loader=LagouJobItemLoader(item=LagouJobItem(),response=response)
        item_loader.add_css("title", ".job-name::attr(title)")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_object_id", get_md5(response.url))
        item_loader.add_css("salary", ".job_request .salary::text")
        item_loader.add_xpath("job_city", "//*[@class='job_request']/p/span[2]/text()")
        item_loader.add_xpath("work_years", "//*[@class='job_request']/p/span[3]/text()")
        item_loader.add_xpath("degree_need", "//*[@class='job_request']/p/span[4]/text()")
        item_loader.add_xpath("job_type", "//*[@class='job_request']/p/span[5]/text()")

        item_loader.add_css("tags", '.position-label li::text')
        item_loader.add_css("publish_time", ".publish_time::text")
        item_loader.add_css("job_advantage", ".job-advantage p::text")
        item_loader.add_css("job_desc", ".job_bt div")
        item_loader.add_css("job_addr", ".work_addr")
        item_loader.add_css("company_name", "#job_company dt a img::attr(alt)")
        item_loader.add_css("company_url", "#job_company dt a::attr(href)")
        item_loader.add_value("crawl_time", datetime.now())
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        return item_loader.load_item()
