import scrapy
import json
import re#正则匹配
from urllib import parse#url的编解码
from ..items import JdItem
from scrapy_redis.spiders import RedisSpider#1.使用redis分布式爬 #5.设置settings里面的配置
#6.redis里面添加key,并传递初始url:lpush jingdong https://gw-e.jd.com/client.action?callback=func&body=%7B%22moduleType%22%3A1%2C%22page%22%3A1%2C%22pageSize%22%3A20%2C%22scopeType%22%3A1%7D&functionId=bookRank&client=e.jd.com&_=1732667213092
#7.启动分布式爬虫:scrapy crawl app
class AppSpider(RedisSpider):#2.继承RedisSpider
    # def __init__(self):
    #     self.page=1
    def __init__(self, *args, **kwargs):#4.分布式爬虫类的初始化
        domain = kwargs.pop("domain", "")
        self.allowed_domains = filter(None, domain.split(","))
        super(AppSpider, self).__init__(*args, **kwargs)
        self.page=1
    name = 'app'
    # allowed_domains = ['channel.jd.com']
    # start_urls = ['https://gw-e.jd.com/client.action?callback=func&body=%7B%22moduleType%22%3A1%2C%22page%22%3A1%2C%22pageSize%22%3A20%2C%22scopeType%22%3A1%7D&functionId=bookRank&client=e.jd.com&_=1732667213092']
    redis_key="jingdong"#3.设置rediskey
    def parse(self, response):
        match = re.search(r'func\((\{.*\})\)', response.text)
        json_str = match.group(1) if match else None
        if json_str is not None:
            json_data=json.loads(json_str)#字符串转json
            obj=JdItem()
            for book in json_data["data"]["books"]:
                obj["title"]=book["bookName"]
                obj["price"]=book["sellPrice"]
                # print(title,price)
                yield obj
            self.page+=1
            next_url = '{{"moduleType":1,"page":{page},"pageSize":20,"scopeType":1}}'.format(page=self.page)#字符串---------编码
            next_url="https://gw-e.jd.com/client.action?callback=func&body="+parse.quote(next_url)+"&functionId=bookRank&client=e.jd.com&_=1732667213092"#编码---------符串
            print(next_url)
            yield scrapy.Request(url=next_url,callback=self.parse,dont_filter=True)