# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging

class SilkdealsPipeline:
    def process_item(self, item, spider):
        return item
    def open_spider(self,spider):
        logging.warning("spider opened from pipeline")
    def close_spider(self,spider):
        logging.warning("spider closed from pipeline")
    @classmethod
    def from_crawler(cls,crawler):
        logging.warning(crawler.settings.get("MONGO_URL"))
