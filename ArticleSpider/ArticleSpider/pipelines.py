# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import codecs
import json
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
import MySQLdb#pip install mysqlclient同步入库
from twisted.enterprise import adbapi#异步入库
class ArticlespiderPipeline:
    def process_item(self, item, spider):
        return item
#图片保存到本地images文件夹，并返回保存地址到front_image_url
class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        if "front_iamge_url" in item:
            image_file_path=""
            for ok,value in results:
                image_file_path=value["path"]
            item["front_image_path"]=image_file_path
        return item
#数据json格式保存到本地(自定义)
class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file=codecs.open("article.json","a",encoding="utf-8")
    def process_item(self,item,spider):
        lines=json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(lines)
        return item
    def spider_closed(self,spider):
        self.file.close()
#将数据导出，这里是倒成json文件（自带的）
class JsonExporterPipeline(object):
    def __init__(self):
        self.file=open("articleexport.json",'wb')
        self.exporter=JsonItemExporter(self.file,encoding="utf-8",ensure_ascii=False)
        self.exporter.start_exporting()
    def process_item(self,item,spider):
        self.exporter.export_item(item)
        return item
    def spider_closed(self,spider):
        self.exporter.finish_exporting()
        self.file.close()
#将数据同步存储到mysql
class MysqlPipeline(object):
    def __init__(self):
        self.conn=MySQLdb.connect("127.0.0.1","root","190023",'articles',charset="utf8",use_unicode=True)
        self.cursor=self.conn.cursor()
    def process_item(self,item,spider):
        insert_sql="""insert into articels_spider(title,url,url_object_id,front_image_path,front_image_url,praise_nums,comment_nums,fav_nums,tags,content,create_date)
        values(%s,%s,%s,%s,%s,%s,,%s,%s,%s,%s,%s)"""
        params=list()
        params.append(item.get("title",""))
        params.append(item.get("url",""))
        params.append(item.get("url_object_id",""))
        params.append(item.get("front_image_path",""))
        front_image_url=",".join(item.get("front_image_url",[]))
        params.append(front_image_url)
        params.append(item.get("praise_nums",0))
        params.append(item.get("comment_nums",0))
        params.append(item.get("fav_nums",0))
        params.append(item.get("tags",""))
        params.append(item.get("content",""))
        params.append(item.get("create_date","1970-07-01"))
        self.cursor.execute(insert_sql,tuple(params))
        self.conn.commit()
        return item
#将数据异步存储到mysql  
class MysqlTwistedPipeline(object):
    def __init__(self,dbpool):
         self.dbpool = dbpool
        
    @classmethod
    def from_setting(cls,settings):
        from MySQLdb.cursors import DictCursor
        dbparms=dict(host=settings["MYSQL_HOST"],db=settings["MYSQL_DBNAME"],user=settings["MYSQL_USER"],passwd=settings["MYSQL_PASSWORD"],charset="utf8",cursorclass=DictCursor,use_unicode=True)
        dbpool=adbapi.ConnectionPool("MySQLdb",**dbparms)
        return cls(dbpool)
    def process_item(self, item, spider):
        #使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider) #处理异常

    def handle_error(self, failure, item, spider):
        #处理异步插入的异常
        print (failure)

    def do_insert(self, cursor, item):
        #执行具体的插入
        #根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql="""insert into articels_spider(title,url,url_object_id,front_image_path,front_image_url,praise_nums,comment_nums,fav_nums,tags,content,create_date)
        values(%s,%s,%s,%s,%s,%s,,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE praise_nums=VALUES(praise_nums)"""
        params=list()
        params.append(item.get("title",""))
        params.append(item.get("url",""))
        params.append(item.get("url_object_id",""))
        params.append(item.get("front_image_path",""))
        front_image_url=",".join(item.get("front_image_url",[]))
        params.append(front_image_url)
        params.append(item.get("praise_nums",0))
        params.append(item.get("comment_nums",0))
        params.append(item.get("fav_nums",0))
        params.append(item.get("tags",""))
        params.append(item.get("content",""))
        params.append(item.get("create_date","1970-07-01"))
        cursor.execute(insert_sql,tuple(params))