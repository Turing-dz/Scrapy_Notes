# text="中文"
# e=text.encode("utf-8")
# print(e)
# d=e.decode("utf-8")
# print(d)
import requests
import os
html=requests.get("http://www.baidu.com")
html.encoding="utf-8"
print(html.text)
print(os.getcwd())#获取当前目录