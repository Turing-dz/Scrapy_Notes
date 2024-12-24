import redis
import pymongo
import json

db_redis = redis.Redis(host="localhost", port="6379", decode_responses=True)
client_mongo = pymongo.MongoClient("mongodb://localhost:27017")
db_mongo = client_mongo["Redis2Mongo"]
col_mongo = db_mongo["C1"]

for i in db_redis.lrange("list2", 0, -1):
    page = {
        # "title": json.loads(i)["title"]
        "value":i
    }
    res = col_mongo.insert_one(page)
    print(res.inserted_id)