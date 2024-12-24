import requests
import re
url="http://zu.fang.com/chuzu/3_482150873_1.htm"#第一层到第二层的链接
headers={
    # "host":"www.fang.com",
    # "referer":"http://zu.fang.com/",
    "connection":"keep-alive",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    # "cookie":"global_cookie=e33cvtloie0dvutlye3opw31m10m3crp22d; __utmc=147393320; __utmz=147393320.1731314072.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; city=www; csrfToken=s61egjJq9xOAXjPRSstO_c8K; __jsluid_s=5a08c8dc0f4500dcbbed1fccad06345d; g_sourcepage=zf_fy%5Exq_pc; __utma=147393320.1895898260.1731314072.1731372443.1731375534.4; otherid=14d0966fed67a19dc7cea5e5dc47a381; __utmb=147393320.21.10.1731375534; unique_cookie=U_e33cvtloie0dvutlye3opw31m10m3crp22d*26"
}
html=requests.get(url,headers=headers)
print(html.text)