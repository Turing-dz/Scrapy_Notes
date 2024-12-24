# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import pymongo.client_options
import pymongo.mongo_client
#保存txt
# class CarPipeline:
#     def __init__(self):
#         self.f=open("cardata.txt","w")
#     def process_item(self, item, spider):
#         # print(item["title"],item["price"])
#         # with open("./cardata.txt","a") as f:
#         #     f.write(item["title"]+item["price"]+"\n")
#         self.f.write(item["title"]+item["price"]+"\n")
#         return item
#     def __delattr__(self, name: str) -> None:
#         self.f.close()
#保存mongodb
class CarPipeline:
    def __init__(self):
        self.client=pymongo.MongoClient("mongodb://localhost:27017")
        self.db=self.client["cheshi"]
        self.col=self.db["cars"]
    def process_item(self, item, spider):
        res=self.col.insert_one(dict(item))
        print(res)
        return item
    def __del__(self, name: str) -> None:
        print("end")