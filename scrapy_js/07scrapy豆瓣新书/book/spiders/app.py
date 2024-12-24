import scrapy
from ..items import BookItem

class AppSpider(scrapy.Spider):
    name = 'app'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/latest']

    def parse(self, response):
        books=response.xpath("//ul[@class='chart-dashed-list']/li")
        for book in books:
            # title=book.xpath(".//h2[@class='clearfix']/a/text()").get()
            link=book.xpath(".//h2[@class='clearfix']/a/@href").get()
            # print(title,link)
            yield scrapy.Request(url=link,callback=self.parse_details)
        next_url=response.xpath("//span[@class='next']/a/@href").get()
        if next_url is not None:
            next_link=response.urljoin(next_url)
            print(next_link)
            yield scrapy.Request(url=next_link,callback=self.parse)
    def parse_details(self,response):
        obj=BookItem()
        obj["title"]=response.xpath("//div[@id='wrapper']/h1/span/text()").get()
        obj["publisher"]=response.xpath("//div[@id='content']//div[@id='info']/a/text()").get()
        # print(title,publisher)
        yield obj