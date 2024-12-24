import scrapy
from ..items import CarItem

class AppSpider(scrapy.Spider):
    name = 'app'
    allowed_domains = ['product.cheshi.com']
    start_urls = ['https://product.cheshi.com/rank/2-0-0-0-1/']

    def parse(self, response):
        # print(response.text)
        # print(response.status)
        # print(response.ip_address)
        print(response.request.headers)
        # item=CarItem()
        # cars=response.xpath("//ul[@class='condition_list_con']/li")
        # for car in cars:
        #     item['title']=car.xpath("./div[@class='m_detail']//a/text()").get()
        #     item['price']=car.xpath("./div[@class='m_detail']//div[@class='pinner_l']/b/text()").get()
        #     # print(item)
        #     yield item
