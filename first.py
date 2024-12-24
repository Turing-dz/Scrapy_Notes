import requests
from bs4 import BeautifulSoup
headers={
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}
def detail_url(url):
	html=requests.get(url,headers=headers)
	soup=BeautifulSoup(html.text,'lxml')
	title=soup.title.text
	compony_name=(soup.select(".com_intro .com-name")[0].text).strip()
	salary=soup.select(".job_money")[0].text
	print(salary)
def crawl():
	for i in range(1,5):
		html=requests.get("https://www.shixiseng.com/interns?page={}&type=intern&keyword=python".format(i),headers=headers)
		soup=BeautifulSoup(html.text,'lxml')
		contents=soup.select('.intern-wrap.intern-item')#20个一样的，之后遍历
		for content in contents:
			url=content.select('.f-l.intern-detail__job a')[0]['href']#拿到每一行的链接，然后使用detail——url函数去处理这个页面
			detail_url(url)
crawl()
