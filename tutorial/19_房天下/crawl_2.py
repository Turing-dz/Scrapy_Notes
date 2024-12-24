import requests
from lxml import etree
import re
from urllib import parse
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from db_1 import sess,House
headers={
    # "host":"www.fang.com",
    # "referer":"https://zu.fang.com/",
    "connection":"keep-alive",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    # "cookie":"global_cookie=e33cvtloie0dvutlye3opw31m10m3crp22d; __utmc=147393320; __utmz=147393320.1731314072.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; city=www; g_sourcepage=zf_fy%5Elb_pc; csrfToken=s61egjJq9xOAXjPRSstO_c8K; __jsluid_s=5a08c8dc0f4500dcbbed1fccad06345d; otherid=2fe8896a3f17d50ad30308701fb9da55; __utma=147393320.1895898260.1731314072.1731370350.1731372443.3; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; unique_cookie=U_e33cvtloie0dvutlye3opw31m10m3crp22d*16; __utmb=147393320.39.10.1731372443"
}
session=requests.session()
session.headers=headers
session.max_redirects = 100

def get_two_element(url):
    pass
#获取第一层页面的数据和链接（第二层页面链接）
def get_element(url):
    html=session.get(url,headers=headers)
    if html.status_code==200:
        tree=etree.HTML(html.text)
        dls = tree.xpath("//dl[contains(@class, 'list') and contains(@class, 'hiddenMap') and contains(@class, 'rel')]")
        for dl in dls:
            title = dl.xpath(".//p[@class='title']/a/text()")
            rent=dl.xpath(".//div[@class='moreInfo']/p/span/text()")
            block=dl.xpath(".//dd[@class='info rel']/div/p[@class='mt12']/span/text()")
            hreflink_half = tree.xpath(".//p[@class='title']/a")[0]
            # # 获取该a标签的文本内容
            href_value = "https://zu.fang.com"+hreflink_half.get('href')
            if title:
                print("out:", title,rent,block,href_value)
    else:
        print("url请求出错")
#获取第一层每各地区共有多少页
def get_number(html):
    soup=etree.HTML(html.text)
    elements = soup.xpath("//div[@class='fanye']/span[@class='txt']")
    if elements:
        pages_text = elements[0].text
    else:
        print("未找到目标元素")
        return None
    re_page=re.compile("\d+")
    number_page=re_page.findall(pages_text)[0]
    if number_page:
        return number_page
    else:
        return None
#进入第一层页面，获取pages
def get_index(url):
    html=session.get(url,headers=headers)
    if html.status_code==200:
        print(html)
        number_page=get_number(html)
        if not number_page:
            number_page=1
        urls_page=[url+"i3{}/".format(i) for i in range(1,int(number_page))]  
        for url_page in urls_page:
            get_element(url_page)  
    else:
        print("url请求出错")
def main():
    urls=["http://zu.fang.com/house-a0{}/".format(i) for i in range(1,17)]
    for url in urls:
        get_index(url)
if __name__=="__main__":
    main()
    session.close()