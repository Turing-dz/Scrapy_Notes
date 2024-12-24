import requests

cookies = {
    'acw_tc': '1a0c399717340654132087978e0040f8d60f732f7f50d36a8dfc2971fa8e9a',
    'Hm_lvt_a19fd7224d30e3c8a6558dcb38c4beed': '1734065415',
    'HMACCOUNT': '56A9DCD1B1C5C105',
    'NR_MAIN_SOURCE_RECORD': '{"locationSearch":"","locationHref":"https://www.newrank.cn/","referrer":"https://www.google.com/","source":30000,"keyword":"seo","firstReferrer":"","firstLocation":"","sourceHref":"https://www.newrank.cn/"}',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22193be5b60a36f7-0d21ec31b9a0578-26011851-3686400-193be5b60a4b3b%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzYmU1YjYwYTM2ZjctMGQyMWVjMzFiOWEwNTc4LTI2MDExODUxLTM2ODY0MDAtMTkzYmU1YjYwYTRiM2IifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22193be5b60a36f7-0d21ec31b9a0578-26011851-3686400-193be5b60a4b3b%22%7D',
    'sajssdk_2015_cross_new_user': '1',
    'Hm_lpvt_a19fd7224d30e3c8a6558dcb38c4beed': '1734065809',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'acw_tc=1a0c399717340654132087978e0040f8d60f732f7f50d36a8dfc2971fa8e9a; Hm_lvt_a19fd7224d30e3c8a6558dcb38c4beed=1734065415; HMACCOUNT=56A9DCD1B1C5C105; NR_MAIN_SOURCE_RECORD={"locationSearch":"","locationHref":"https://www.newrank.cn/","referrer":"https://www.google.com/","source":30000,"keyword":"seo","firstReferrer":"","firstLocation":"","sourceHref":"https://www.newrank.cn/"}; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22193be5b60a36f7-0d21ec31b9a0578-26011851-3686400-193be5b60a4b3b%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzYmU1YjYwYTM2ZjctMGQyMWVjMzFiOWEwNTc4LTI2MDExODUxLTM2ODY0MDAtMTkzYmU1YjYwYTRiM2IifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22193be5b60a36f7-0d21ec31b9a0578-26011851-3686400-193be5b60a4b3b%22%7D; sajssdk_2015_cross_new_user=1; Hm_lpvt_a19fd7224d30e3c8a6558dcb38c4beed=1734065809',
    'Pragma': 'no-cache',
    'Referer': 'https://www.newrank.cn/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'from': '303',
}

response = requests.get('https://www.newrank.cn/ranklist/xiaohongshu/1/7', params=params, cookies=cookies, headers=headers)
print(response.text)