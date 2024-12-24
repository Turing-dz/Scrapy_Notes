i: 手抓饭
from: zh-CHS
to: en
useTerm: false
domain: 0
dictResult: true
keyid: webfanyi
sign: caeee37658ded40b15c427b294858516
     'd8256dac54b71eba2a991128388f9f7a'
client: fanyideskweb
product: webfanyi
appVersion: 1.0.0
vendor: web
pointParam: client,mysticTime,product
mysticTime: 1733816549765
keyfrom: fanyi.web
mid: 1
screen: 1
model: 1
network: wifi
abtest: 0
yduuid: abcdefg







import requests

cookies = {
    'OUTFOX_SEARCH_USER_ID': '386146828@154.55.113.38',
    'OUTFOX_SEARCH_USER_ID_NCOO': '1376155476.3606348',
    'DICT_DOCTRANS_SESSION_ID': 'MDRjMjM0YzktMmJkZi00MWVlLWI4ZTEtNjAyMjExMWM5NGFl',
    '_uetsid': 'da2eaac0b6c311ef9bc3356040d99eab',
    '_uetvid': 'da2eae60b6c311efbc78557568d7a790',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'OUTFOX_SEARCH_USER_ID=386146828@154.55.113.38; OUTFOX_SEARCH_USER_ID_NCOO=1376155476.3606348; DICT_DOCTRANS_SESSION_ID=MDRjMjM0YzktMmJkZi00MWVlLWI4ZTEtNjAyMjExMWM5NGFl; _uetsid=da2eaac0b6c311ef9bc3356040d99eab; _uetvid=da2eae60b6c311efbc78557568d7a790',
    'Origin': 'https://fanyi.youdao.com',
    'Pragma': 'no-cache',
    'Referer': 'https://fanyi.youdao.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'i': '手抓饭',
    'from': 'zh-CHS',
    'to': 'en',
    'useTerm': 'false',
    'domain': '0',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': 'caeee37658ded40b15c427b294858516',
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': '1733816549765',
    'keyfrom': 'fanyi.web',
    'mid': '1',
    'screen': '1',
    'model': '1',
    'network': 'wifi',
    'abtest': '0',
    'yduuid': 'abcdefg',
}

response = requests.post('https://dict.youdao.com/webtranslate', cookies=cookies, headers=headers, data=data)
print(response.text)