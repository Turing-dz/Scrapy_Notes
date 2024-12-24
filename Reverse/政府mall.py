import requests
import time
import math
import csv
now=round(time.time())#保留13位
for pageNum in range(1,4):
    cookies = {
        'CT6T': 'b72411',
        'Hm_lvt_139c628de301d6f3d54245fc7c8ba583': '1733889459,1733982070',
        'HMACCOUNT': 'C5A65D297B2FF8C6',
        'Hm_lpvt_139c628de301d6f3d54245fc7c8ba583': str(now),
    }
    # Sgm-Context="".concat(t, ";").concat(t)
    headers = {
        'Referer': 'https://mkt.zycg.gov.cn/mall-view/product/search?businessType=1&cid=1000290',
        'Sgm-Context': '610671251444615800;610671251444615800',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    json_data = {
        'queryPage': {
            'platformId': 20,
            'pageSize': 28,
            'pageNum': pageNum,
        },
        'orderType': 'desc',
        'homeType': '10',
        'isAggregation': False,
        'publishType': '1',
        'orderColumn': 'saleCount',
        'cid': 1000290,
        'businessType': '1',
        'cids': [],
    }

    response = requests.post(
        'https://mkt.zycg.gov.cn/proxy/trade-service/mall/search/searchByParamFromEs',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    for result in response.json()["data"]["itemList"]["resultList"]:
        skuId=result["skuId"]
        shopName=result["shopName"]
        skuName=result["skuName"]
        #每个skuid商品的page获取
        headers['Referer']=f'https://mkt.zycg.gov.cn/mall-view/product/detail?skuid={skuId}'
        json_data_pageNum = {
            'skuId': skuId,
            'salesArea': '北京市',
            'publishType': 1,
            'blacklistStatus': 0,
            'queryPage': {
                'platformId': 20,
                'pageSize': 1,
                'pageNum': 1,
            },
        }
        count = requests.post(
            'https://mkt.zycg.gov.cn/proxy/trade-service/mall/search/getSaleStatusAndAgentList',
            cookies=cookies,
            headers=headers,
            json=json_data_pageNum,
        ).json()["data"]["count"]
        page = math.ceil(count / 10)
        for i in range(page):
            json_data_phone = {
                'skuId': skuId,
                'salesArea': '北京市',
                'publishType': 1,
                'blacklistStatus': 0,
                'shopName': '',
                'queryPage': {
                    'platformId': 20,
                    'pageSize': 10,
                    'pageNum': i+1,
                },
            }
            response = requests.post('https://mkt.zycg.gov.cn/proxy/trade-service/mall/search/querySkuAgentListFromEs',
                cookies=cookies,
                headers=headers,
                json=json_data_phone,
            )
            for phone in response.json()["data"]["itemAgentList"]["resultList"]:
                with open("zf_mall_ytj.csv","a", newline='') as f:#, newline=''表示中间不空一行
                    f_csv=csv.writer(f)#写入缓存
                    data=[skuId,shopName,skuName,phone["agentName"],phone["agentPhone"]]
                    f_csv.writerow(data)#写入一行
            
        