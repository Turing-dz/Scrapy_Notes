import requests
import json
import pymongo
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
client=pymongo.MongoClient("mongodb://localhost:27017")
db=client["douban"]
col=db["files"]#链接
def parse(url,params):
    res=requests.get(url,headers=headers,params=params)
    # print(json.dumps(res.json(),ensure_ascii=False,indent=4))
    for item in res.json():
        data={
            "title":item["title"],
            "rank":item["rank"],
            "release_date":item["release_date"],  
        }
        obj=col.insert_one(data)#增加1条数据
        print(obj.inserted_id)
if __name__=="__main__":
    url="https://movie.douban.com/j/chart/top_list"
    for i in range(0,201,20):
        params={
            "type":"24",
            "interval_id": "100:90",
            "action":" ",
            "start": f"{i}",
            "limit":" 20"
        }
        parse(url,params)