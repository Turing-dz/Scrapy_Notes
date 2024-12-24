import requests
import re
def parse(url):
    # url="https://www.ygdy8.net/html/gndy/oumei/index.html"
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    res=requests.get(url,headers=headers)
    #返回的页面有乱码，经过搜索，查到charset=gb2312，所以对res进行编码转换
    res.encoding="gb2312"
    # print(res.text)
    exp=re.compile('<td height="26">.*?href="(.*?)"',re.S)
    # print(exp.findall(res.text))
    # exp_name=re.compile("◎译　　名　(.*?)<br />")
    # exp_year=re.compile("◎年　　代　(.*?)<br />")
    exp_all=re.compile("◎译　　名　(.*?)<br />.*?◎年　　代　(.*?)<br />",re.S)

    # for link in exp.findall(res.text):
    #     link="https://www.ygdy8.net/"+link
    #     res_detail=requests.get(link,headers=headers)
    #     res_detail.encoding="gb2312"
    #     # print(exp_name.findall(res_detail.text))
    #     # print(exp_year.findall(res_detail.text))
    #     print(exp_all.findall(res_detail.text))
    exp_next=re.compile("<a href='(.*?)'>下一页</a>")
    if len(exp_next.findall(res.text))!=0:
        url_next= "https://www.ygdy8.net/html/gndy/oumei/"+exp_next.findall(res.text)[0]
        print(url_next)
        parse(url_next)
if __name__=="__main__":
    parse("https://www.ygdy8.net/html/gndy/oumei/index.html")
        