#session维护会话，获取cookie后会自动保存携带
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
session=requests.session()
session.post(url_login,headers=headers,data=data)#自动保存携带获取到的cookies(session没有维护headers，所以下面访问时要携带headers)
url="https://my.cheshi.com/user/"
res=session.get(url,headers=headers)
print(res.text)