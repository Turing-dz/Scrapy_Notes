from typing import Iterable
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
from time import sleep 
class ExampleSpider(scrapy.Spider):
    name = "example"
    def start_requests(self):
        yield SeleniumRequest(url="https://google.com",wait_time=3,screenshot=True,callback=self.parse)
    def parse(self, response):
        # img=response.meta['screenshot']
        # with open("screenshot.png",'wb') as f:
        #     f.write(img)
        driver=response.meta['driver']#获取页面元素，首先需要driver
        search_input = driver.find_element(By.XPATH, "//textarea[@class='gLFyf']") 
        search_input.send_keys("hello world")
        search_input.send_keys(Keys.ENTER)
        # 获取点击后的response页面
        new_response=driver.page_source
        
        # 将新的页面内容传递给 Scrapy 进行解析
        response = scrapy.Selector(text=new_response)
        # driver.save_screenshot("after_filling_input.png")
        for link in response.xpath("//a[@jsname='UWckNb']"):
            yield {'URL':link.xpath(".//@href").get()}
