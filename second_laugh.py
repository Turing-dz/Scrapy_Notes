import requests
from bs4 import BeautifulSoup
headers={
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}
for i in range(1,3):
	html=requests.get("https://xiaohua.zol.com.cn/lengxiaohua/{}.html".format(i),headers=headers)
	#print(html.text)#页面源代码
	#使用bs4解析页面内容(select,find_all选择器)
	soup=BeautifulSoup(html.text,'lxml')
	titles=soup.select(".article-summary>.article-title")
	for title in titles:
		print(title.select("a")[0].text)