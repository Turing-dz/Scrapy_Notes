# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import pymongo
import sqlite3
# class ImdbPipeline:
#     def open_spider(self,spider):
#         self.client=pymongo.MongoClient("mongodb+srv://<zhuodeng0023>:<ng8ADhingmEQHf9m>@cluster0.bi6ki.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#         self.db=self.client["IMDB"]
#     def process_item(self, item, spider):
#         self.db[self.collection_name].insert_one(item)
#         return item
#     def close_spider(self,spider):
#         self.client.close()
class SqliteImdbPipeline:
    def open_spider(self,spider):
        self.connection=sqlite3.connect("imdb.db")
        self.cursor=self.connection.cursor()
        try:
            self.cursor.execute('''
                            CREATE TABLE best_movies(
                                title TEXT,
                                movie_url TEXT
                            )
                            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
           pass
    def process_item(self, item, spider):
        self.cursor.execute('''
                            INSERT INTO best_movies (title,movie_url) VALUES(?,?)
                            ''',(item.get("title"),item.get("movie_url")))
        self.connection.commit()
        return item
    def close_spider(self,spider):
        self.connection.close()    