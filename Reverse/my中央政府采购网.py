import requests
import time
now=round(time.time())#保留13位
businessType=1
cid=1000290
Sgm_Context="111116774841114140;111116774841114140"
platformId=20
pageNum=1


cookies = {
    'Hm_lvt_139c628de301d6f3d54245fc7c8ba583': '1733889459',
    'HMACCOUNT': '007BA746F933A8E1',
    'CT6T': '2e6011',
    'Hm_lpvt_139c628de301d6f3d54245fc7c8ba583': str(now),
}
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json ; charset=UTF-8',
    'Origin': 'https://mkt.zycg.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://mkt.zycg.gov.cn/mall-view/product/search?businessType={businessType}&cid={cid}',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sgm-Context': Sgm_Context,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'queryPage': {
        'platformId': platformId,
        'pageSize': 28,
        'pageNum': pageNum,
    },
    'orderType': 'desc',
    'homeType': '10',
    'isAggregation': True,
    'publishType': '1',
    'orderColumn': 'saleCount',
    'cid': cid,
    'businessType': '1',
    'cids': [],
}
response = requests.post(
   'https://mkt.zycg.gov.cn/proxy/trade-service/mall/search/searchByParamFromEs',
   cookies=cookies,
   headers=headers,
   json=json_data,
)
for item in response.json()["data"]["itemList"]["resultList"]:
    # print(item)
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'Hm_lvt_139c628de301d6f3d54245fc7c8ba583=1733889459; HMACCOUNT=007BA746F933A8E1; CT6T=576b61; Hm_lpvt_139c628de301d6f3d54245fc7c8ba583=1733889594',
        'Origin': 'https://mkt.zycg.gov.cn',
        'Pragma': 'no-cache',
        'Referer': f'https://mkt.zycg.gov.cn/mall-view/product/detail?skuid={item["skuId"]}',################DZ--------url
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sgm-Context': '344714140450141000;344714140450141000',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'platformId': f'{item["platformId"]}',
        'customerType': '1',
        'accountId': '123456789',
        'shopId': f'{item["shopId"]}',
    }
    # print(headers,data)
    response_2 = requests.post(
        'https://mkt.zycg.gov.cn/proxy/platform/shop/customer/queryCustomer',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(item["shopName"])
    print(response_2.json()["data"][0]["telephone"])