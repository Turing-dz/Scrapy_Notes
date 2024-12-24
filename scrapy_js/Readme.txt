pip install scrapy   (scrapy自带xpath功能，获取元素内容需要.get())                         
scrapy startproject car .                (items.py数据模型;middlewares.py中间件;piplines.py数据存储;settings.py设置文件)
scrapy genspider app https://product.cheshi.com/rank/2-0-0-0-1/
scrapy crawl app


配置settings.py
LOG_LEVEL="ERROR"
ROBOTSTXT_OBEY = False
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
打开ITEM_PIPELINES和MIDDLEWARES（如果用到的话）

模型items.py
title = scrapy.Field()
...
在app里面导入模型类(from ..items import CarItem)，创建空对象，然后把爬取的数据赋值给对象,最后yield item（此时item对象就到了pipelines）

数据存储piplines.py（用到piplines就需要到settings里面打开ITEM_PIPELINES）
app里面爬到的数据封装成对象item后yield到这里，在这里进行保存


中间件middlewares.py（用到middlewares就需要到settings里面打开SPIDER_MIDDLEWARES或者DOWNLOADER_MIDDLEWARES）
随机useragent，代理ip，使用selenium，添加cookie
主要是在DownloaderMiddleware类的process_request和process_response方法
随机useragent:
def process_request(self, request, spider):
    usa=["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"]
    request.headers["Use-Agent"]=random.choice(usa)
    return None


#crawlspider
scrapy genspider -t crawl app https://seller.cheshi.com/beijing/
rules匹配访问链接

#redis
数据类型（string,hash,list,set,zset）
#scrapy-redis分布式爬虫(pip install scrapy-redis)



#1.反爬措施
1.基于身份识别的反爬（user-agent，refer，captcha验证码，必备参数）
2.基于爬虫行为的反爬（单位时间内请求数量，相邻两次请求之间的时间间隔，蜜罐陷阱）
3.通过对数据加密进行反爬（对文字加密，对请求参数进行加密，对响应数据加密）
对文字加密：数据图片化（ocr），对文字进行编码（unicode,utf-8,ascii），自定义字体，css偏移文字加密
hex(num)#10-----16   ox
bin(num)#10------2     ob
字符集（ascii   english   7bits ，Unicode   所有语言   2bytes，utf-8     所有语言  基于unicode可变长度1-4bytes英文1bytes中文2bytes，gbk  中文）
ord（“A”）#字符------ascii
chr（65）#ascii------字符