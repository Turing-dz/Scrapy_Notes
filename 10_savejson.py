import requests
import json#不带s串，带s文件，dump to json,load json to

# (Python 对象或字典转换为 JSON 格式)json.dumps 返回 JSON 字符串,json.dump将数据写入json文件中
# zd={"name":"zoe","age":28}
# a=json.dumps(zd)
# print(a)
# with open ("s_j.json","w") as f:
#     json.dump(zd,f)


# #(JSON 格式的字符串转换为 Python 对象或字典)json.loads ,json.load（将 JSON 格式的数据从文件中读取并转换为 Python 对象或字典）
# print(json.loads(a))
# with open("s_j.json","r") as f:
#     content=json.load(f)
#     print(content)






# #抓取腾讯新闻（ajax异步请求,返回的是json格式的数据，通过loads换成）
# headers={
#     "referer":"https://news.qq.com/",
# 	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
#  "cookie":"pac_uid=0_k1pEbd8mtTTJr; current-city-name=bj; _qimei_uuid42=18b0708360b10035390af8215313fb22cda0e8387a; _qimei_fingerprint=0b1cb33603487c79ebb5793fe548b9b3; _qimei_q36=; _qimei_h38=527f790f390af8215313fb220200000ad18b07; suid=user_0_k1pEbd8mtTTJr; lcad_appuser=D5E0B4A4C0BEAF81; lcad_LZCturn=58; lcad_LPHLSturn=3; lcad_o_minduid=3QudaMBY5_CJ2Rf7mWkv5UBxmPTsEoID; lcad_LPSJturn=921; lcad_LBSturn=173; lcad_LVINturn=855; lcad_LPLFturn=251; lcad_LDERturn=146"
# }
# def get_html():
#     url="https://i.news.qq.com/i/getONSDict?wuji_appid=PCQQCOM&wuji_appkey=53856f37d2ac4c1e874bd58763d6fcc9&query_key=games"
#     html=requests.get(url,headers=headers)
#     if html.status_code==200:
#         contents=json.loads(html.text)["data"]["games"]["data"]
#         for c in contents:
#             title=c["title"]
#             print(title)
#     else:
#         print("网站请求失败")
# get_html()



import csv#数据读写csv
headers=["z","f","g"]#写
rows=[("aa","bb","cc"),("dd","rr","ww"),("ff","yy","jj")]
with open("save.csv","a", newline='') as f:#, w写入，a追加，newline=''表示中间不空一行
    f_csv=csv.writer(f)#写入缓存
    f_csv.writerow(headers)#写入一行
    f_csv.writerows(rows)#写入多行
with open("save.csv","r",encoding="utf-8") as f:#读
    f_csv=csv.reader(f)#python内置的csv解析缓存
    next(f_csv)#跳过第一行，title
    for i in f_csv:
        print(i)
import xlrd,xlwt#数据读写excel,需要pip
from docx import Document#数据读写word,需要pip install python-docx