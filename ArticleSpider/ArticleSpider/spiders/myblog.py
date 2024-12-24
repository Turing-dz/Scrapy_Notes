import scrapy
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
import time
from mouse import move,click
class MyblogSpider(scrapy.Spider):
    name="myblog"
    allowed_domains = ["news.cnblogs.com"]
    start_urls = ["https://news.cnblogs.com"]
    def start_requests(self):
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
        #2.登录（selenium点击）
        browser.get("https://account.cnblogs.com/signin")
        browser.find_element(By.CSS_SELECTOR,".mat-form-field-infix.ng-tns-c47-4 input").send_keys("Turing-dz")
        browser.find_element(By.CSS_SELECTOR,".mat-form-field-infix.ng-tns-c47-5 input").send_keys("190023dz")
        browser.find_element(By.CSS_SELECTOR,".mat-focus-indicator.action-button.ng-tns-c122-1.mat-flat-button.mat-button-base.mat-primary").click()
        time.sleep(3)
        move(1281,915)
        click()
        time.sleep(60)
        #2.登录（requests请求）
        
    def parse(self, response):
        pass
    
    