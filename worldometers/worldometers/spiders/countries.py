import scrapy
import logging
# from scrapy.shell import inspect_response
# from scrapy.utils.response import open_in_browser
import logging
class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]
    def parse(self, response):
        countries=response.xpath("//td/a")
        for country in countries:
            name=country.xpath(".//text()").get()
            link=country.xpath("./@href").get()
            
            absolute_link=f"https://www.worldometers.info{link}"#1.字符串拼接-域名链接
            yield scrapy.Request(url=absolute_link)
            absolute_link=response.urljoin(link)#2.response的urljoin方法拼接-域名链接
            yield scrapy.Request(url=absolute_link)
            yield response.follow(url=link)# 3.response的follow方法直接访问（内部拼接-域名链接）
            yield response.follow(url=link,callback=self.parse_country,meta={'country_name':name})#对首url访问后，再follow link，并对link返回的子页面的html在parse_country函数里处理
            # yield response.follow(url="https://www.worldometers.info/world-population/china-population/",callback=self.parse_country,meta={'country_name':"china"})#对首url访问后，再follow link，并对link返回的子页面的html在parse_country函数里处理
    def parse_country(self,response):
        logging.info(response.url)
        name=response.request.meta['country_name']#response.request.meta获取上层传递的参数
        rows=response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year=row.xpath(".//td[1]/text()").get()
            population=row.xpath("./td[2]/strong/text()").get()
            yield{
                'name':name,
                'year':year,
                'population':population
            }
        # inspect_response(response, self)
        # open_in_browser(response)   
        # logging.info(response.status)
            
       
