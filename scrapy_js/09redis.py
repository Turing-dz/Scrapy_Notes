import redis#pip install redis
db=redis.Redis(host="localhost",port="6379",decode_responses=True)
#string 存value
db.set("name","小12")#添加1个键值对
print(db.get("name"))#获取1个值
db.mset({"name1":"老王","age1":"老衲年方28"})#添加多个键值对
print(db.mget("name1","name","age1"))#获取多个值
# #hash 存key-value
db.hset("hash1","key1","value1")#添加
db.hset("hash1","key2","value2")
db.hset("hash1","key3","value3")
print(db.hget("hash1","key2"))#获取hash中key对应的值
print(db.hgetall("hash1"))#获取hash中所有的键值对
# list 存list
db.lpush("list1",1,2,3)#倒序插入，先进后出
db.rpush("list2",2,3,4,5)#顺序插入，先进先出
print(db.llen("list1"))#list的长度
print(db.lrange("list1",0,-1))#lrange key start stop(-1 在 Redis 中是一个特殊的索引，表示列表的最后一个元素)
#set
db.sadd("set1",55,66,77,55)
print(db.scard("set1"))#scard获取set的长度
print(db.smembers("set1"))#smembers获取set的所有元素
#zset
db.zadd("zset1", {"zoe": 22, "jodie": 11})#Redis 的 Sorted Set（有序集合）要求每个成员（member）都关联一个分数（score）
print(db.zcard("zset1"))
print(db.zrange("zset1",0,-1,withscores=True))#[('jodie', 11.0), ('zoe', 22.0)]
