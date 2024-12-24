import requests
import math

cookies = {
    'Hm_lvt_139c628de301d6f3d54245fc7c8ba583': '1733889459',
    'HMACCOUNT': '007BA746F933A8E1',
    'CT6T': 'a508b1',
    'Hm_lpvt_139c628de301d6f3d54245fc7c8ba583': '1733895938',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json ; charset=UTF-8',
    # 'Cookie': 'Hm_lvt_139c628de301d6f3d54245fc7c8ba583=1733889459; HMACCOUNT=007BA746F933A8E1; CT6T=a508b1; Hm_lpvt_139c628de301d6f3d54245fc7c8ba583=1733895938',
    'Origin': 'https://mkt.zycg.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://mkt.zycg.gov.cn/mall-view/product/detail?skuid=2479480',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sgm-Context': '727912791445099900;727912791445099900',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'skuId': 2479480,
    'salesArea': '北京市',
    'publishType': 1,
    'blacklistStatus': 0,
    'queryPage': {
        'platformId': 20,
        'pageSize': 1,
        'pageNum': 1,
    },
}

response = requests.post(
    'https://mkt.zycg.gov.cn/proxy/trade-service/mall/search/getSaleStatusAndAgentList',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{"skuId":2479480,"salesArea":"北京市","publishType":1,"blacklistStatus":0,"queryPage":{"platformId":20,"pageSize":1,"pageNum":1}}'.encode()
# response = requests.post(
#    'https://mkt.zycg.gov.cn/proxy/trade-service/mall/search/getSaleStatusAndAgentList',
#    cookies=cookies,
#    headers=headers,
#    data=data,
# )
count=response.json()["data"]["count"]
page = math.ceil(count / 10)
print(page)