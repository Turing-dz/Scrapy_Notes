import requests
from urllib import parse
import time 
import sys
import io

# 修改标准输出编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
headers={
	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
	"referer":"https://github.com/login",
	"cookie":"_octo=GH1.1.1048949994.1726204352; _device_id=f036f579621f1b3200db3080f210de7b; GHCC=Required:1-Analytics:1-SocialMedia:1-Advertising:1; MicrosoftApplicationsTelemetryDeviceId=0b2700da-fefd-44d6-9d57-aeadb682d04f; preferred_color_mode=light; tz=Asia%2FShanghai; fs_uid=#o-1FH3DA-na1#5847570654113792:1565405744240102493:::#/1762410976; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=no; _gh_sess=ODrojN8KyhzAr1C6dehuz%2B7CgQCrKLlllxznvjESHugRf%2B1eRpa8mxYjVJHHQwQVbuNEFBbvytx%2BupVPuAB8L9H9r4vNjtor06b0l%2F0b9Woo08E5VI9Hf2XrYpA6k1ozW7AZZZL8XrTP7vRt3IFiVr%2B1lDQHp4AHr8upoGWdRaFKtCez0NK3A%2BRAwqAdd7lroKKEUAeMGxMjenp2tun94nP66d9GcFcvFQnGKZvVdotITbDJGKZ44MsQmRXC2SMXSQjrMIEaI6j6RT5e9%2FBAIyKKuhysxZ8ncRvjQhSfMXSlTgeOq82S44Oi2%2FRBJvPRVIwGh6yyBXepxl8uv18Q%2FqCUz1oW68e3XtOsAH6JrquGqEcHSeOzJZweCOoBUQ5rxIdR5EPZMx9kQn8GqtzeKzpkw0jEZAIdYDy%2B4q%2FmH6Wg9A4KpApezyLlP%2FuwZfMIWnje%2Blu%2B9xb%2FDk%2BhRd3iVYs35PhipcsJFaAkzdUAe%2FhfnJEw--zYjf1qMRdw2w953f--6Reugx%2BBD2hKvZYzVHCRHg%3D%3D"
}
def save_html(text):
	with open("login_after.html","w",encoding="utf-8") as f:
		f.write(text)
def post_login_github():
	url="https://github.com/session"
	data={
	"commit": "Sign in",
	"authenticity_token": "UeyeFszQkTtljGHZK9cZqDHHZtgBkUyT/bR37Q1ebNIVNzh4RXr9yu+WllxbRNE7i+0CGFjbSJJ/95cnEcVtSg==",
	"login": "hhhhhhhhh@163.com",
	"password": "PASSWORDdz",
	"webauthn-conditional": "undefined",
	"javascript-support": "true",
	"webauthn-support": "supported",
	"webauthn-iuvpaa-support": "supported",
	"return_to": "https://github.com/login",
	"timestamp": "{}".format(time.time()),
	"timestamp_secret": "6416e730e0e1bd3a500f8b5ce523cb93dca1961c9bbda15d6407f862a8fa01c0",
	}
	html=requests.post(url,headers=headers,data=data)
	if html.status_code==200:
		save_html(html.text)
	else:
		print(html.status_code)
if __name__=="__main__":
	post_login_github()