import requests
from bs4 import BeautifulSoup#lxml,re
import sys
import io

from doubandb import Book,sess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')# 修改标准输出编码为UTF-8
headers={
	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
	# "referer":"https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=60&type=T"
}
def download(name,image_url):
	img_content=requests.get(image_url,headers=headers)
	if not os.path.exists("doubanIm"):
		os.makedirs("doubanIm")
	with open("./doubanIm/{}.jpg".format(name),"wb") as f:
		f.write(img_content.content)
def parse_html(text):
	soup=BeautifulSoup(text,"lxml")
	books=soup.select(".subject-item")
	for book in books:
		# print(book)
		title=book.select_one(".info h2 a").text.strip().replace(" ","").replace("\n","")
		info=book.select_one(".info div.pub").text.strip().replace(" ","").replace("\n","")
		rate=book.select_one(".rating_nums").text.strip().replace(" ","").replace("\n","")
		pl=book.select_one(".pl").text.strip().replace(" ","").replace("\n","")
		introduce = book.select_one(".info p").text.strip().replace(" ", "").replace("\n", "") if book.select_one(".info p") else ""
		img_url=book.select_one(".pic a img")["src"]
		# download(title,img_url)
		print(title,info,rate,pl,introduce)
		try:
			book_data=Book(title=title,info=info,star=rate,pl=pl,introduce=introduce)
			sess.add(book_data)
			sess.commit()
   
		except Exception as e:
			print(e)
			sess.rollback()
			

def get_html(url):
	html=requests.get(url,headers=headers)
	if html.status_code==200:
		parse_html(html.text)
	else:
		print("获取网站失败")
for i in range(0,300,20):
	url="https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={}&type=T".format(i)
	# print(url)
	get_html(url)