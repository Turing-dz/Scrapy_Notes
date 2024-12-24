import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AppSpider(CrawlSpider):
    name = 'app'
    allowed_domains = ['seller.cheshi.com']
    start_urls = ['https://seller.cheshi.com/beijing/']

    rules = (
        Rule(LinkExtractor(allow=r'seller.cheshi.com/\d+',deny=r"seller.cheshi.com/\d+/.+"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title=response.xpath("//div[@class='clearfix']//a[@class='name']/text()").get()
        print(title,response.url)
