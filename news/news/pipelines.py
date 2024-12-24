# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.exporters import CsvItemExporter
class NewsPipeline:
    def __init__(self):
        self.file = open("news_data.csv", "wb")
        self.exporter=CsvItemExporter(self.file,encoding="utf-8")#查看源代码，搜索charset，确定页面的编码格式
        self.exporter.start_exporting()
    def close_spider(self,spider):
        self.exporter.finish_exporting()#进程关闭掉
        self.file.close()#文件关闭掉
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
