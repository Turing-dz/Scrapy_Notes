#1.携带cookies
import requests
url="https://my.cheshi.com/user/"
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
cookies="pv_uid=1732254874878; cheshi_UUID=01JD96ZEWPDK2ZKK8X3WGFFPVS; cheshi_pro_city=MV%2FljJfkuqxfMV%2FkuJzln47ljLpfYmVpamluZw%3D%3D; Hm_lvt_8fe47348e12ba11be217fd389b115472=1732254888,1732494411; HMACCOUNT=0F938E3E8702278B; lv=1732674538; vn=7; Hm_lvt_ed9cf33799965fb6c868762ac84e663e=1732674587; Hm_lpvt_ed9cf33799965fb6c868762ac84e663e=1732674590; cheshi_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6ImNoZXNoaV9oNV9zaWduIn0.eyJpc3MiOiJodHRwczpcL1wvYXBpLmNoZXNoaS5jb20iLCJhdWQiOiJodHRwczpcL1wvYXBpLmNoZXNoaS5jb20iLCJqdGkiOiJjaGVzaGlfaDVfc2lnbiIsImlhdCI6MTczMjY3NDY2OSwibmJmIjoxNzMyNjc0NzI5LCJleHAiOjE3MzMyNzk0NjksInVpZCI6IjkxMDcxNDIifQ.ihAUr-0-7HEFedu-u23BlcstiaynxHrBAVDBXqnAW_E; cheshi_user_authv2=MzI2NDUyNAlsaXR0bGVaCXYyCWJjZDYzMWQ4NDZlMTQ4ZWQwY2UzZThhMTFkYTE2YmQxCTE3MzI2NzQ2NjkJNDgyN2JjMTgwZjg5MzIyNDg4MDAyYzg3NjYwOGRmNTY=; cheshi_user_info=OTEwNzE0MglsaXR0bGVaCXYyCWJjZDYzMWQ4NDZlMTQ4ZWQwY2UzZThhMTFkYTE2YmQxCTE3MzI2NzQ2NjkJNDgyN2JjMTgwZjg5MzIyNDg4MDAyYzg3NjYwOGRmNTYJCQl3YW5nc2hhbmdjaGVzaGk=; cheshi_user_info_for_index=OTEwNzE0MglsaXR0bGVaCXYyCWJjZDYzMWQ4NDZlMTQ4ZWQwY2UzZThhMTFkYTE2YmQxCTE3MzI2NzQ2NjkJNDgyN2JjMTgwZjg5MzIyNDg4MDAyYzg3NjYwOGRmNTYJCQl3YW5nc2hhbmdjaGVzaGk=; Hm_lpvt_8fe47348e12ba11be217fd389b115472=1732674672; PHPSESSID=bd0f056bb72ef681c01a68b853bde882; pv_source=; cheshi_user_prevLogintime=1732674716; pv_cheshit=1732674722341"
cookies={ item.split("=")[0] : item.split("=")[1] for item in cookies.split("; ")}#字符串转换成dict
print(cookies)
cookies=requests.utils.cookiejar_from_dict(cookies)#把cookie转换成dick，然后通过requests接口传递cookies
res=requests.get(url,headers=headers,cookies=cookies)
print(res.text)

#2.通过登录接口(调试时保留日志)，拿到response的set-cookie，直接使用cookies获取数据
import requests

url_login="https://api.cheshi.com/services/common/api.php?api=login.Login"
data={
    "act": "login",
"mobile": "hhhhhhhhh",
"source": "pc",
"password": "PASSWORDdz",
"hold_time": "yes",
}
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res=requests.post(url=url_login,headers=headers,data=data)
# print(res.cookies)
url="https://my.cheshi.com/user/"
res=requests.get(url,headers=headers,cookies=res.cookies)
print(res.text)
