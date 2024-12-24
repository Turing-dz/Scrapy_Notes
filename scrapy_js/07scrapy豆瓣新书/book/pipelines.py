# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class BookPipeline:
    def __init__(self):
        self.client=pymongo.MongoClient("mongodb://localhost:27017")
        self.db=self.client["douban"]
        self.col=self.db["book"]
    def process_item(self, item, spider):
        self.col.insert_one(dict(item))
        return item
    def __del__(self):
        print("end")