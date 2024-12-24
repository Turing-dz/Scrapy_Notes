#pip install pymongo
import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")#客户端client
db=client["app"]#数据库db
col=db["C1"]#集合Collection
# user={
#     "name":"zoe",
#     "age":"28",
#     "email":"1888@163.com"
# }
# obj=col.insert_one(user)#增加1条数据
# print(obj.inserted_id)
users=[
    {
    "name":"zoe1",
    "age":281,
    "email":"1888@163.com"
},
    {
    "name":"zoe2",
    "age":228,
    "email":"1888@163.com"
},
    {
    "name":"zoe3",
    "age":238,
    "email":"1888@163.com"
} 
]
objs=col.insert_many(users)#增加多条数据，文档 (document)
print(objs.inserted_ids)

# users=col.find()#查询所有
# for user in users:
#     print(user)

#条件查询
# objs=col.find({"name":"zoe"})
objs=col.find({"age":{"$gt":20}})#年龄大于20#$regex正则匹配
for user in objs:
    print(user)