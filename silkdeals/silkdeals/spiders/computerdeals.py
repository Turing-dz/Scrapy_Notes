from typing import Iterable
import scrapy
from scrapy_selenium import SeleniumRequest

class ComputerdealsSpider(scrapy.Spider):
    name = "computerdeals"
    # allowed_domains = ["lickdeals.net"]
    # start_urls = ["https://slickdeals.net/computer-deals/"]
    def start_requests(self):
        yield SeleniumRequest(url='https://slickdeals.net/computer-deals/',wait_time=3,callback=self.parse)
    def parse(self, response):
        products=response.xpath("//ul[@class='bp-p-filterGrid_items']/li")
        for product in products:
            yield{
                'name':product.xpath("./div/a[2]/text()").get(),
                'link':'https://slickdeals.net'+product.xpath("./div/a[2]/@href").get(),
                'price':product.xpath("./div/span[@class='bp-p-dealCard_price']/text()").get(),
                'store_name':product.xpath("normalize-space(./div/span[@class='bp-c-card_subtitle']/text())").get(),
            }
        # response.xpath("//ul[@class='bp-p-filterGrid_items']/li").get().click()
        
        
 