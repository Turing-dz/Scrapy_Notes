import requests
from lxml import etree
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
def parse(url):
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.text)
    items = tree.xpath('//div[@class="rank_d_list borderB_c_dsh_clearfix"]//div[@class="rank_d_b_name"]')
    for item in items:
        print(item)
if __name__ == "__main__":
    parse("https://www.zongheng.com/rank/details.html?rt=3&d=1")