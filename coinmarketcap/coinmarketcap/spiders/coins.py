from typing import Iterable
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
from time import sleep
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class CoinsSpider(CrawlSpider):
    name = "coins"
    allowed_domains = ["coinsmarketcap.com"]
    # start_urls = ["https://coinsmarketcap.com"]
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    # rules = (Rule(LinkExtractor(restrict_xpaths="//tbody/tr/td[3]/div/a"), callback="parse_item", follow=True),)
    def set_user_agent(self,request,spider):
        request.headers['User-Agent']=self.user_agent
        return request
    def start_requests(self):
        yield SeleniumRequest(url="https://coinsmarketcap.com",wait_time=3,screenshot=True,callback=self.parse_item)
    rules =(Rule(LinkExtractor(restrict_xpaths='//table/tbody/tr/td[3]/div/a'), callback="parse_item", follow=True,process_request='set_user_agent'),)
    def parse_item(self, response):
        # scrapy.shell.inspect_response(response, self)
        print(response.url)
    #    yield {
    #        "name":response.xpath("//span[@data-role='coin-name']/text()").get(),
    #        "rank":response.xpath("(//div[@data-role='chip-content-item']/text())[1]").get(),
    #        "price":response.xpath("//span[@data-test='text-cdp-price-display']/text()").get()
    #    }
