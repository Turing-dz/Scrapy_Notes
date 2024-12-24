import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Protocol.KDF import scrypt
import base64
import time
import execjs
time_stap=round(time.time()*1000)
def decrypt_aes_cbc(ciphertext_base64, key, iv):
    ciphertext = base64.b64decode(ciphertext_base64)# 将 base64 编码的密文解码为字节
    cipher = AES.new(key, AES.MODE_CBC, iv)# 创建 AES 解密器，使用 CBC 模式和给定的 IV
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)# 解密并去除填充
    return decrypted_data.decode('utf-8')# 将解密后的字节转为字符串（假设是 UTF-8 编码）

#请求头参数加密
e_data={
    "ts": time_stap,
    "type": "12",
    "IS_IMPORT": 1,
    "pageSize": 3
}
portal_sign=execjs.compile(open('./13AES头部参数逆向.js','r',encoding='utf-8').read()).call('d',e_data)

print(portal_sign)



headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://ggzyfw.fujian.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ggzyfw.fujian.gov.cn/index/newList/?type=12',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'portal-sign': portal_sign,
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# json_data = {
#     'type': '12',
#     'IS_IMPORT': 1,
#     'pageSize': 3,
#     # 'ts': 1733729093668,
#     'ts': time_stap
# }

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
data = '{"type":"12","IS_IMPORT":1,"pageSize":3,"ts":{time_stap}}'
response = requests.post('https://ggzyfw.fujian.gov.cn/FwPortalApi/Article/PageList', headers=headers, json=e_data)
print(response.json())
key = "EB444973714E4A40876CE66BE45D5930"  # 替换为实际密钥
iv = "B5A8904209931867"    # 替换为实际 IV
decrypted_message = decrypt_aes_cbc(response.json()["Data"],key.encode('utf-8'), iv.encode('utf-8'))# 解密
print("Decrypted message:", decrypted_message)