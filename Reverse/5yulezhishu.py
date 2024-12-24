import requests
import execjs
import json
cookies = {
    'Hm_lvt_2873e2b0bdd5404c734992cd3ae7253f': '1733380167',
    'HMACCOUNT': 'C5CE8D1FB35E7C3B',
    'mobile_iindex_uuid': 'd2b3cc84-f9c3-5981-9113-e25033a41f7d',
    'Hm_lpvt_2873e2b0bdd5404c734992cd3ae7253f': '1733387367',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_2873e2b0bdd5404c734992cd3ae7253f=1733380167; HMACCOUNT=C5CE8D1FB35E7C3B; mobile_iindex_uuid=d2b3cc84-f9c3-5981-9113-e25033a41f7d; Hm_lpvt_2873e2b0bdd5404c734992cd3ae7253f=1733387367',
    'Pragma': 'no-cache',
    'Referer': 'https://www.chinaindex.net/ranklist/4',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'UUID': 'd2b3cc84-f9c3-5981-9113-e25033a41f7d',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'funcID': 'undefined',
    'incognitoMode': '0',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'channel': 'movielist',
    'sign': '5f3cce6a40c09a221b21104cc98436a3',
}

response = requests.get(
    'https://www.chinaindex.net/iIndexMobileServer/mobile/movie/objectFansRank',
    params=params,
    cookies=cookies,
    headers=headers,
)
data=response.json()["data"]
lastFetchTime=response.json()["lastFetchTime"]
ctx=execjs.compile(open('./5yulezhishu.js','r',encoding='utf-8').read()).call('dataFilter',data,lastFetchTime)
for i in json.loads(ctx)["listOfRank"]:#str------------json(json.loads())
    print(i["object_name"])