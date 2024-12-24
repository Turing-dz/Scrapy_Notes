#异步爬取，使用正则匹配JavaScript内容（页面内容通过javascript函数镶嵌到页面的,通过正则表达式，匹配出镶嵌的内容，然后findall）
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import re
headers={
    "referer":"https://www.zhihu.com/billboard",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "cookie":"_zap=ea4062df-2cee-44eb-ae3c-1fa7f0f4d8c1; d_c0=AGAStGEWORmPTtbCeygKjZaI4i-zcr7fwTI=|1726107802; __snaker__id=jXDGz56iZjSQl2S8; q_c1=c1c1a8a2de7f4c0593b03d60d2c61431|1726197783000|1726197783000; _xsrf=1e7198ad-fdda-4aa0-bac3-ba8f265446d9; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1731311791; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1731311791; HMACCOUNT=FB731F83F91CF8D1; SESSIONID=ENEywW4oZlXmDLNN7vU2XfoT6akax4tk61wePdgei3F; JOID=Wl0SA02fmgL9KVMtSpX5n_Q-2AJc19ZAglAJGyLL-1iXaxFuBiAnMpIqXChLdX88qlgliY0vECNoiGE1DIqKkow=; osd=WlkQAEifngD-LFMpSJb8n_A82wdc09RDh1ANGSHO-1yVaBRuAiIkN5IuXitOdXs-qV0ljY8sFSNsimIwDI6IkYk=; BEC=5468d338557f9906d5c8cdb6d5cda0d3"
}
ids=re.compile('"cardId":"Q_(\d+)',re.S|re.I)
re_content=re.compile('"excerptArea":{"text":"(.*?)"}')
async def get_html():
    url="https://www.zhihu.com/billboard"
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            text=await resp.text()#异步爬取到页面源码
    soup=BeautifulSoup(text,"lxml")
    hotlists=soup.select(".HotList-item")
    for hot in hotlists:
        title=hot.select_one(".HotList-itemTitle").text
        print(title)
    contents = re_content.findall(text)
    for c in contents:
        print(c)
        print('-'*20)
    hot_ids = ids.findall(text)
    for u in hot_ids:
        url = "https://www.zhihu.com/question/{}?utm_division=hot_list_page".format(u)
        print(url)        
if __name__=="__main__":
    loop=asyncio.get_event_loop()#开启异步
    loop.run_until_complete(get_html())
    loop.close()