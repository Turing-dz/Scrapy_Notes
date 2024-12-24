from typing import Iterable
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = "best_movies"
    allowed_domains = ["imdb.com"]
    # start_urls = ["https://www.imdb.com/search/title/?groups=top_250&sort=user_rating"]
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/search/title/?groups=top_250&sort=user_rating',
                             headers={
                                 'User-Agent':self.user_agent
                             })
        #process_request是对请求的处理
    rules = (Rule(LinkExtractor(restrict_xpaths="//a[@class='ipc-title-link-wrapper']"), callback="parse_item", follow=True,process_request='set_user_agent'),#这里提取a的href的时候不用@href，直接就拿到了链接
            #  Rule(LinkExtractor(restrict_xpaths="//a[@class='ipc-chip ipc-chip--on-baseAlt']"), follow=True,process_request='set_user_agent')#这个a链接到下一页，没有callback自动使用第一个rule的规则
             )
    def set_user_agent(self,request,spider):
        request.headers['User-Agent']=self.user_agent
        return request
    def parse_item(self, response):
    #    print(response.url)
        yield {
            'title':response.xpath("//span[@class='hero__primary-text']/text()").get(),
            'year':response.xpath("(//ul[@class='ipc-inline-list ipc-inline-list--show-dividers sc-ec65ba05-2 joVhBE baseAlt']/li[@class='ipc-inline-list__item']/a[@class='ipc-link ipc-link--baseAlt ipc-link--inherit-color'])[1]/text()").get(),
            'duration':response.xpath("(//ul[@class='ipc-inline-list ipc-inline-list--show-dividers sc-ec65ba05-2 joVhBE baseAlt']/li[@class='ipc-inline-list__item'])[3]/text()").get(),
            'gener': response.xpath("//a[@class='ipc-chip ipc-chip--on-baseAlt']/span/text()").getall(),  # 使用 getall() 提取所有标签,返回列表数据
            'rating':response.xpath("(//span[@class='sc-d541859f-1 imUuxf'])[1]/text()").get(),
            'movie_url':response.url,
            'User-Agent':response.request.headers['User-Agent']
        }
