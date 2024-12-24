import requests
from Crypto.Cipher import AES#pip install pycryptodome
import base64
from Crypto.Util.Padding import unpad 
cookies = {
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22193a941d038126b-004216e561b1c29c-26011851-3686400-193a941d039135a%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com.hk%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzYTk0MWQwMzgxMjZiLTAwNDIxNmU1NjFiMWMyOWMtMjYwMTE4NTEtMzY4NjQwMC0xOTNhOTQxZDAzOTEzNWEifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22193a941d038126b-004216e561b1c29c-26011851-3686400-193a941d039135a%22%7D',
    'acw_tc': '784e2ca917337114833915416e3bc815e02aa1f6b53fc02982502e625b2bd4',
    'sensorsdata2015jssdkchannel': '%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D',
    'wz_uuid': 'X/40b63c827b58d6f8033a67bdd8791a21',
    'Hm_lvt_9ea3e7293b7c088e0d2c88874b63e7dd': '1733711485',
    'HMACCOUNT': '6386D125432C1D7F',
    'x-web-ip': '120.246.94.2, 121.199.80.157, 120.78.44.156, 100.121.99.234',
    'accessToken': '',
    'token': '',
    'Hm_lpvt_9ea3e7293b7c088e0d2c88874b63e7dd': '1733711795',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22193a941d038126b-004216e561b1c29c-26011851-3686400-193a941d039135a%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com.hk%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkzYTk0MWQwMzgxMjZiLTAwNDIxNmU1NjFiMWMyOWMtMjYwMTE4NTEtMzY4NjQwMC0xOTNhOTQxZDAzOTEzNWEifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22193a941d038126b-004216e561b1c29c-26011851-3686400-193a941d039135a%22%7D; acw_tc=784e2ca917337114833915416e3bc815e02aa1f6b53fc02982502e625b2bd4; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; wz_uuid=X/40b63c827b58d6f8033a67bdd8791a21; Hm_lvt_9ea3e7293b7c088e0d2c88874b63e7dd=1733711485; HMACCOUNT=6386D125432C1D7F; x-web-ip=120.246.94.2, 121.199.80.157, 120.78.44.156, 100.121.99.234; accessToken=; token=; Hm_lpvt_9ea3e7293b7c088e0d2c88874b63e7dd=1733711795',
    'device-id': 'Bu9THfACEOG8RovNHCVBBzxJkbCZzoxG4KwLlLQRG0S75VjEg9+IfIeHtP+h8mL8FpTfdDAb4/B44r9CMq1s7TA==',
    'eagleeye-pappname': 'fyw9n1jhpf@07619cbd1f4e9df',
    'eagleeye-sessionid': 'wmmC14kwg29fqn80qy3LwqL4nt2s',
    'eagleeye-traceid': '1d899d39173371181133110204e9df',
    'h5version': 'v1.0.0',
    'origin': 'https://www.qizhidao.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.qizhidao.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sensordeviceid': '193a941d038126b-004216e561b1c29c-26011851-3686400-193a941d039135a',
    'sensorsdistinctid': '193a941d038126b-004216e561b1c29c-26011851-3686400-193a941d039135a',
    'signature': '80820a7fe0664629b1e0374ea7ef7581.HDuHqT',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'user-agent-web': 'X/40b63c827b58d6f8033a67bdd8791a21',
}

json_data = {
    'searchKey': '华为',
    'type': 0,
    'pageSize': 10,
    'current': 1,
    'platform': 1,
}

response = requests.post(
    'https://app.qizhidao.com/qzd-bff-app/app/index/search/all/pc',
    cookies=cookies,
    headers=headers,
    json=json_data,
    
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
data = '{"searchKey":"华为","type":0,"pageSize":10,"current":1,"platform":1}'.encode()
response = requests.post(
   'https://app.qizhidao.com/qzd-bff-app/app/index/search/all/pc',
   cookies=cookies,
   headers=headers,
   data=data,
)
data1=response.json()["data1"]
def AES_decrypt(data1):
    html = base64.b64decode(data1)
    key = b"40w42rjLEXxYhxRn"
    aes = AES.new(key, AES.MODE_ECB)
    info = aes.decrypt(html)
    decrypt_data = unpad(info, 16).decode()
    return decrypt_data
data_out=AES_decrypt(data1)
print(data_out)



