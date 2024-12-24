# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags
from ArticleSpider.settings import SQL_DATETIME_FORMAT, SQL_DATE_FORMAT
class ArticleItemLoader(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()
class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    create_date = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field()
    comment_nums = scrapy.Field()
    fav_nums = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()
def remove_splash(value):#去掉job——city里面的斜线
    return value.replace("/","")  
def handle_jobaddr(value):
    addr_list=value.split("\n")
    addr_list=[item.strip() for item in addr_list if item.strip()!="查看地图"]
    return "".join(addr_list)  
class LagouJobItem(scrapy.Item):
    title = scrapy.Field()          # 职位标题
    url = scrapy.Field()            # 职位详情页的 URL
    url_object_id = scrapy.Field()  # URL 的唯一标识符
    salary = scrapy.Field()         # 薪资
    job_city = scrapy.Field(input_processor=MapCompose(remove_splash))       # 工作城市
    work_years = scrapy.Field(input_processor=MapCompose(remove_splash))     # 工作年限
    degree_need = scrapy.Field(input_processor=MapCompose(remove_splash))    # 学历要求
    job_type = scrapy.Field()       # 职位类型
    publish_time = scrapy.Field()   # 发布时间
    job_advantage = scrapy.Field()  # 职位优势
    job_desc = scrapy.Field()       # 职位描述
    job_addr = scrapy.Field(input_processor=MapCompose(remove_tags,handle_jobaddr))       # 工作地址
    company_name = scrapy.Field()   # 公司名称
    company_url = scrapy.Field()    # 公司官网 URL
    tags = scrapy.Field(input_processor=Join(","))           # 职位标签
    crawl_time = scrapy.Field()     # 爬取时间
    def get_insert_sql(self):
        insert_sql = """
            insert into lagou_job(title, url, url_object_id, salary, job_city, work_years, degree_need,
            job_type, publish_time, job_advantage, job_desc, job_addr, company_name, company_url,
            tags, crawl_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE salary=VALUES(salary), job_desc=VALUES(job_desc)
        """
        params = (
            self["title"], self["url"], self["url_object_id"], self["salary"], self["job_city"],
            self["work_years"], self["degree_need"], self["job_type"],
            self["publish_time"], self["job_advantage"], self["job_desc"],
            self["job_addr"], self["company_name"], self["company_url"],
            self["job_addr"], self["crawl_time"].strftime(SQL_DATETIME_FORMAT),
        )

        return insert_sql, params
        
class LagouJobItemLoader(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()