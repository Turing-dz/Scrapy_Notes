import scrapy
from scrapy import Request
from urllib import parse
import requests
import json
import re
from ArticleSpider.items import ArticlespiderItem
from ArticleSpider.utils.common import get_md5
from scrapy.loader import ItemLoader
from ArticleSpider.items import ArticleItemLoader
from selenium import webdriver
import time
class CnblogsSpider(scrapy.Spider):
    name = "cnblogs"
    allowed_domains = ["news.cnblogs.com"]
    start_urls = ["https://news.cnblogs.com"]
    
    def start_requests(self):
        browser=webdriver.Chrome(executable_path="C:/Users/dz/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        browser.get("https://account.cnblogs.com/signin")
        browser.find_element_by_css_selector(".mat-form-field-infix.ng-tns-c47-4 input").send_keys("Turing-dz")
        browser.find_element_by_css_selector(".mat-form-field-infix.ng-tns-c47-5 input").send_keys("190023dz")
        browser.find_element_by_css_selector(".mat-focus-indicator.action-button.ng-tns-c122-1.mat-flat-button.mat-button-base.mat-primary").click()
        time.sleep(60)
    def parse(self, response):
        #url=response.xpath('//div[@id="news_list"]//h2[@class="news_entry"]/a/@href').extract_first("")#1.xpath
        #urls=response.css('div#news_list h2 a::attr(href)').extract()#2.css选择器
        post_nodes=response.css("#news_list .news_block")#首先拿到news——block列表
        for post_node in post_nodes:
            image_url = post_node.css('.entry_summary a img::attr(src)').extract_first("")#然后拿到每个block里的img的链接
            post_url=post_node.css('h2 a::attr(href)').extract_first("")#和他里面的链接
            yield Request(url=parse.urljoin(response.url,post_url),meta={"front_image_url":image_url},callback=self.parse_detail)#然后将链接和域名进行拼接，并把image——url参数传递过去,然后调用callback函数进行处理
        #然后获取下一页的block列表
        # next_url=response.css("div.pager a:last-child::text").extract()
        # if next_url=="Next >":
        #     next_url=response.css("div.pager a:last-child::attr(href)").extract()
        #     yield Request(url=parse.urljoin(response.url,next_url),callback=self.parse)
        next_url = response.xpath("//a[contains(text(),'Next >')]/@href").extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

        
    def parse_detail(self, response):
        # article_item = ArticlespiderItem()
        match_re = re.match(".*?(\d+)", response.url)
        if match_re:
            post_id = match_re.group(1)
        #     title = response.css("#news_title a::text").extract_first("")
        #     create_date = response.css("#news_info .time::text").extract_first("")
        #     content = response.css("#news_content").extract()[0]
        #     tag_list = response.css(".news_tags a::text").extract()
        #     tags = ",".join(tag_list)
        #     
        #     # html = requests.get(parse.urljoin(response.url, "NewsAjax/GetAjaxNewsInfo?contentId={}".format(post_id)))
        #     article_item["title"] = title
        #     article_item["create_date"] = create_date
        #     article_item["content"] = content
        #     article_item["tags"] = tags
        #     if response.meta.get("front_image_url", ""): 
        #         article_item["front_image_url"] = [response.meta.get("front_image_url", "")]#图片链接要去pipeline下载，所以必须转换成列表格式
        #     else:
        #         article_item["front_image_url"] = []
        #     article_item["url"]=response.url
            #使用itemload加载item
            front_image_url = response.meta.get("front_image_url", "")  # 文章封面图
            item_loader =ArticleItemLoader(item=ArticlespiderItem(), response=response)
            item_loader.add_css("title", ".entry-header h1::text")
            item_loader.add_value("url", response.url)
            item_loader.add_value("url_object_id", get_md5(response.url))
            item_loader.add_css("create_date", "p.entry-meta-hide-on-mobile::text")
            item_loader.add_value("front_image_url", [front_image_url])
            item_loader.add_css("praise_nums", ".vote-post-up h10::text")
            item_loader.add_css("comment_nums", "a[href='#article-comment'] span::text")
            item_loader.add_css("fav_nums", ".bookmark-btn::text")
            item_loader.add_css("tags", "p.entry-meta-hide-on-mobile a::text")
            item_loader.add_css("content", "div.entry")

            article_item = item_loader.load_item()
            yield Request(url=parse.urljoin(response.url, "/NewsAjax/GetAjaxNewsInfo?contentId={}".format(post_id)),callback=self.parse_nums,meta={"article_item":article_item})
    def parse_nums(self,response):
        j_data = json.loads(response.text)
        article_item=response.meta.get("article_item","")
        praise_nums = j_data["DiggCount"]
        fav_nums = j_data["TotalView"]
        comment_nums = j_data["CommentCount"]
        article_item["prise_nums"]=praise_nums
        article_item["fav_nums"]=fav_nums
        article_item["comment_nums"]=comment_nums
        article_item["url_object_id"]=get_md5(article_item['url'])
        yield article_item