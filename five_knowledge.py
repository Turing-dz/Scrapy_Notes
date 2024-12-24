import sys
import io

# 修改标准输出编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# import requests
# html=requests.get("http://www.baidu.com")
# html.encoding="utf-8"
# print(html.status_code)
# print(html.text)
#查看网站技术栈
# import builtwith
# from pprint import pprint
# url="https://www.baidu.com"
# res=builtwith.builtwith(url)
# pprint(res)
#requests课程
import requests
from uuid import uuid4#根据电脑时钟生成不重复的随机数
from urllib import parse#9.python2中的urllib(urllib.parse.urljoin,quote,urlsplit,urlparse)
# base="http://www.baidu.com/"
# snil="/123.jpg"
# print(parse.urljoin(base,snil))#url拼接
base="http://www.baidu.com?wd="
wd="快代理"
print(parse.urljoin(base,parse.quote(wd)))#url字符转码（文字转%E5%BF%AB%E4%BB%A3%E7%90%86）
print(parse.unquote("%E5%BF%AB%E4%BB%A3%E7%90%86"))#转回文字
print(parse.urlsplit("http://www.baidu.com/%E5%BF%AB%E4%BB%A3%E7%90%86"))#url切分，返回对象,与urlparse类似
print(parse.urlparse("http://www.baidu.com/%E5%BF%AB%E4%BB%A3%E7%90%86"))
#4.下载图片音视频，一般都需要headers，否则认证不通过
headers={"connection":"keep-alive",
		"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
		"Referer":"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=&st=-1&fm=index&fr=&hs=0&xthttps=111110&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E4%BD%A0%E5%A5%BD",
		"Cookie":"PSTM=1726108606; BAIDUID=E1FBAA04A5433997B25979E9904EA160:FG=1; BIDUPSID=ED8137F5257D6A0A8D7AE53F70091D8E; BDUSS=WJFbzB2Q0dLfkoxYlQ3bHYwMDFEYzREaXdaeGtFejU4ZE0xN0ZLclY3T0NaMFpuSVFBQUFBJCQAAAAAAAAAAAEAAAD~grc~wMTIy2R6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILaHmeC2h5nW; BDUSS_BFESS=WJFbzB2Q0dLfkoxYlQ3bHYwMDFEYzREaXdaeGtFejU4ZE0xN0ZLclY3T0NaMFpuSVFBQUFBJCQAAAAAAAAAAAEAAAD~grc~wMTIy2R6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILaHmeC2h5nW; H_PS_PSSID=61008_61027_61022_61036_61077; BAIDUID_BFESS=E1FBAA04A5433997B25979E9904EA160:FG=1; delPer=0; BA_HECTOR=84042l05a504al0l8k8k0h8l1u5t161jim9291v; ZFY=ZGm4:B:AOIf0c8xb5fzOmSjcEMxXutapGS18SfcL0zehU:C; BDRCVFR[fq555l35Iot]=OjjlczwSj8nXy4Grjf8mvqV; ab_sr=1.0.1_ODcxZDY5MzIzMTZlMzMyZGQyOTk1YTQyYzk4NDJiZDBhNjA3M2ZlNjcyNmM0N2E2NmI1NzdjNDkwMzVhMjIzMThhOWExNDk3YTY5YTQwOWYwOTBkMTQ5ZDczOGZhZGUyMzhjNGY5Y2Y1YTdlOGM5YjM1MWIwNDkxZDVhYjQxMWExNGE5MTVhNzhmZTM2OGQwMDEwODZmMTdkNDEwOWZjMjZmNDExMTI2YjQ3OWI3MzQ1NGY3ODA1MGZkY2Q0YzU5; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=7; H_WISE_SIDS=61077"
		}
#5.每次访问虽然cookie一样，但也是多次访问，使用session，多次请求都在同一个会话里面，减少tcp握手和资源损耗，速度更快,容易被识别到爬虫
session=requests.session()
session.headers=headers
#7.使用ip代理
proxies={
	"http": "http://202.101.213.95:23437",
	"https":"https://202.101.213.95:23437"
}
#8.post上传文件{"file":(文件名+文件，文件格式，额外参数)}
files={"file":("test",open("./imgs/06c3335c-4a7f-4a55-875c-ce8a3a8062f7.jpg","rb"),"image",{"Expires":"65535"})}
def post_file(url):
	html=requests.post(url,files=files)
	if html.status_code==200:#这个200必须是数字，不能是字符串
		print(html.text)
	else:
		print("error")
def get_html(url):
	# html=requests.get(url)
	# html=requests.get(url,params={"wd":"川普"})#1.get请求传参
	# html=requests.post(url,data={"name":"川普","pwd":"123"})#2.post请求传参
	# html=requests.get(url)#3.ajax交互的json数据请求
	# html=requests.get(url,headers=headers)#4.下载图片音视频
	# html=session.get(url)#5.使用session，多次请求都在同一个会话里面
	# html=requests.get(url，verify=False)#6.忽略https证书验证,关闭验证
	html=requests.get(url,proxies=proxies,timeout=3)#7.使用ip代理
	if html.status_code==200:
		html.encoding="utf-8"
		# print(html.text)
		content=html.json()
		# for c in content["idlist"][0]["newslist"]:
		# 	print(c["id"],c["title"])
		print(content)
		for c in content["data"]:
			try:
				image_url=c["middleURL"]
				download(image_url)
			except:
				pass
	else:
		print("get error")
def download(image_url):
	print("download {}...".format(image_url))
	# img_content=requests.get(image_url,headers=headers)#拿到图片链接再次请求
	img_content=session.get(image_url)
	with open("./imgs/{}.jpg".format(uuid4()),"wb") as f:
		# for chunk in img_content.iter_content(225):#二进制流要用b，225字节
		# 	if chunk:
		# 		f.write(chunk)
		f.write(img_content.content)
	return
if __name__=='__main__':
	# url="https://baidu.com"
	# url="https://baidu.com/s"#get请求传参
	# url="http://httpbin.org/post"#post请求传参
	# url="https://i.news.qq.com/gw/event/pc_hot_ranking_list?ids_hash=&offset=0&page_size=51&appver=15.5_qqnews_7.1.60&rank_id=hot"#ajax交互的json数据请求
	# url="https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7993220761642791215&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E4%BD%A0%E5%A5%BD&queryWord=%E4%BD%A0%E5%A5%BD&cl=2&lm=&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=30&rn=30&gsm=1e&1730942958407="#下载图片音视频，本质上下载二进制流（百度图片ajax获取json数据）
	url="http://httpbin.org/post"#8.post上传文件
	# post_file(url)
	# get_html(url)