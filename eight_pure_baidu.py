import sys
import io
import requests
from bs4 import BeautifulSoup
from urllib import parse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
headers={
	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
}
def parse_html(text):
	soup = BeautifulSoup(text,"lxml")
	results = soup.select('div.result.c-container')
	baidu_result = soup.select('div.result-op.c-container.xpath-log')
	for result in results:
		title = result.select_one('h3 a').text
		href = result.select_one('h3 a')['href']
		print(title, href)
	for baidu in baidu_result:
		title = baidu.select_one('h3 a').text
		href = baidu.select_one('h3 a')['href']
		print(title, href)
def get_baidu(url):
	html=requests.get(url,headers=headers)
	if html.status_code==200:
		parse_html(html.text)
		# print("ok")
	else:
		print("请求出现错误")
if __name__=="__main__":
	keyword=parse.quote(input("请输入要查找的内容>>>"))
	url="https://www.baidu.com/s?wd={}".format(keyword)
	get_baidu(url)