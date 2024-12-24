import scrapy
from scrapy.linkextractors import LinkExtractor#链接提取器
from scrapy.spiders import CrawlSpider, Rule#规则
from news.items import NewsItem#要爬取的数据
#出现403forbid问题，在settings里面添加了user-agent
class News163Spider(CrawlSpider):
    name = 'news163'
    allowed_domains = ['news.163.com', 'www.163.com']  # 因为下一层的url和news不同域，所以添加 www.163.com 到允许的域名,或者直接使用['163.com']，否则出现twisted问题
    start_urls = ['http://news.163.com/']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.163.com/[a-z]*?/article/.*?.html'), callback='parse_item', follow=True),
    )#正则匹配url，回调函数，follow的意思是是否深入
    



    def parse_item(self, response):
        item=NewsItem()#把获取的数据装进去
        item['news_thread']=response.url.strip().split("/")[-1][:-5]
        self.get_title(response,item)#title的取装封装到了方法里，这里直接调用方法
        self.get_time(response,item)
        self.get_source(response,item)
        self.get_source_url(response,item)
        self.get_text(response,item)
        self.get_url(response,item)
        return item
    def get_title(self,response,item):
        title=response.css("title::text").extract()
        if title:
            print("title:{}".format(title[0]))
            item["news_title"]=title[0]
    def get_time(self,response,item):
        time=response.css("div.post_info::text").extract()
        if time:
            print("time:{}".format(time[0].strip().replace("\u3000来源:","")))
            item["news_time"]=time[0].strip().replace("\u3000来源:","")
    def get_source(self,response,item):
        source=response.css(".post_info a::text").extract()
        if source:
            print("source:{}".format(source[0]))
            item["news_source"]=source[0]
    def get_source_url(self,response,item):
        source_url=response.css(".post_info a::attr(href)").extract()#::attr(href)
        if source_url:
            print("source_url:{}".format(source_url[0]))
            item["source_url"]=source_url[0]
    def get_text(self,response,item):
        text=response.css(".post_body p::text").extract()
        if text:
            item["news_body"]=text
    def get_url(self,response,item):
        url=response.url
        if url:
            item["news_url"]=url