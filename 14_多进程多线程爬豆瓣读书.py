#每类书籍开一个进程，每个进程开多个线程跑（因为io密集）
import urllib.parse
import requests
from bs4 import BeautifulSoup
import multiprocessing
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import urllib
headers={
	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
	# "referer":"https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=60&type=T"
}
def get_link(url):
    print("当前进程：{}".format(multiprocessing.Process.pid))
    try:
        response = requests.get(url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, "lxml")
        books = soup.select(".subject-item")
        for book in books:
            title = book.select_one(".info h2 a").text.strip().replace(" ", "").replace("\n", "")
            print(title)
    except Exception as e:
        print(f"Error fetching {url}: {e}")


def th(tag):#多线程
    with ThreadPoolExecutor(max_workers=5) as excutorT:
        urls=[]
        for i in range(0,300,20):
            tag_q=urllib.parse.quote(tag)
            url = f"https://book.douban.com/tag/{tag_q}?start={i}&type=T"
            urls.append(url)
        futures=[excutorT.submit(get_link,item) for item in urls]
        for future in futures:
            future.result()
        
if __name__=="__main__":
    tags=["小说","文学"]
    with ProcessPoolExecutor(max_workers=2) as executorP:#多进程
        futures=[executorP.submit(th,tag) for tag in tags]
        for future in futures:
            future.result()