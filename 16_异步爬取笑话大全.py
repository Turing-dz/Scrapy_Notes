#使用aiohttp取代requests
import aiohttp#pip install aiohttp
import asyncio
from bs4 import BeautifulSoup
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
async def crawl(i):
    print("正在爬取：",i)
    url="https://xiaohua.zol.com.cn/baoxiao/{}.html".format(i)
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            # print(resp.status)
            text=await resp.text()
    soup=BeautifulSoup(text,"lxml")
    lists=soup.select(".article-summary .article-title a")
    for list in lists:
        print(list.get_text())
if __name__=="__main__":
    loop=asyncio.get_event_loop()
    tasks=[crawl(i) for i in range(1,10)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
