import requests
import execjs
import json
cookies = {
    'Hm_lvt_b966fe201514832da03dcf6cbf25b8a2': '1733367326',
    'HMACCOUNT': '43D7FCC8A4C6643B',
    'acw_tc': '1a0c65d717333794010945469e00a70236bff23ee9543640e9bda439f699d6',
    'Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2': '1733379403',
    'ssxmod_itna': 'eqmx9D0mD=0QnDBPxB4+b+q0==VKYvPeYemYwK=D/KDfo4iNDnD8x7YDv+fHD0gexbUiBRc3+fYB3rLPwFOi8d4hFhB8eaDU4i8DCMresrDeWtD5xGoDPxDeDAmqGaDb4DrcdqGPyn2LvkAxiOD7eDXxGCDQ9G44DaDGpkq7Dr2hDDBO+oqWYYqDi3U1HHotB+DiHqy=0DUxG1DQ5Dsg46YBKD0aM6Yny1jS8ALG9h540OD0IwcZc+WeysgaFATj03ejiexr9rqn0D/Y44=7095jr5d0rx8jxBXBw9kd2o9qDWoQhK4D',
    'ssxmod_itna2': 'eqmx9D0mD=0QnDBPxB4+b+q0==VKYvPeYemYwKG9WMi8DBu72D7p=uMIH7GF99Wqi=4L6uHv85Qt0yqpKoBkr6z=QKw8XxY74k0GfqDGTW7ef+/2nf9F5UMKEpMU91=qK/4f9A/bd8h2iqm7UfDuUftEikr7S+Xt/fI43TmuSu67S+Ql9nYjIW=q2uTsjhdX9fAtZ05eoAUI9RK4A8664+Dcmf5/bPyRU6HF=bXzGAIS905hSfvR01hG9R2zCiQuiK=yFBafUpg6U+Hs9P3CNNQCgLlsiXyuX=I63kZOr6XONWa/1Z8pE3kW5S=0ihjD9Dh7UDSDvmIq4vhD+Hpiel0U7GzEAqbpSireUYaDG2D2KFGybaYAW4jnoTO7FgD8O=3eDFqD+hDxD===',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_b966fe201514832da03dcf6cbf25b8a2=1733367326; HMACCOUNT=43D7FCC8A4C6643B; acw_tc=1a0c65d717333794010945469e00a70236bff23ee9543640e9bda439f699d6; Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2=1733379403; ssxmod_itna=eqmx9D0mD=0QnDBPxB4+b+q0==VKYvPeYemYwK=D/KDfo4iNDnD8x7YDv+fHD0gexbUiBRc3+fYB3rLPwFOi8d4hFhB8eaDU4i8DCMresrDeWtD5xGoDPxDeDAmqGaDb4DrcdqGPyn2LvkAxiOD7eDXxGCDQ9G44DaDGpkq7Dr2hDDBO+oqWYYqDi3U1HHotB+DiHqy=0DUxG1DQ5Dsg46YBKD0aM6Yny1jS8ALG9h540OD0IwcZc+WeysgaFATj03ejiexr9rqn0D/Y44=7095jr5d0rx8jxBXBw9kd2o9qDWoQhK4D; ssxmod_itna2=eqmx9D0mD=0QnDBPxB4+b+q0==VKYvPeYemYwKG9WMi8DBu72D7p=uMIH7GF99Wqi=4L6uHv85Qt0yqpKoBkr6z=QKw8XxY74k0GfqDGTW7ef+/2nf9F5UMKEpMU91=qK/4f9A/bd8h2iqm7UfDuUftEikr7S+Xt/fI43TmuSu67S+Ql9nYjIW=q2uTsjhdX9fAtZ05eoAUI9RK4A8664+Dcmf5/bPyRU6HF=bXzGAIS905hSfvR01hG9R2zCiQuiK=yFBafUpg6U+Hs9P3CNNQCgLlsiXyuX=I63kZOr6XONWa/1Z8pE3kW5S=0ihjD9Dh7UDSDvmIq4vhD+Hpiel0U7GzEAqbpSireUYaDG2D2KFGybaYAW4jnoTO7FgD8O=3eDFqD+hDxD===',
    'Pragma': 'no-cache',
    'Referer': 'https://ctbpsp.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'province': '',
    'industry': '',
    'type__1017': 'n4+hDKAKD5YvPQqGKG=D/tF4BKAsyYOnmnAoD',
}

response = requests.get(
    'https://ctbpsp.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/2',
    params=params,
    cookies=cookies,
    headers=headers,
)

response_json = response.json()
response_json_str = json.dumps(response_json)  # 将 JSON 转换为字符串
# ctx=execjs.compile(open('./4fujiansheng.js','r',encoding='utf-8').read()).call('b',response.json())
ctx=execjs.compile(open('./4fujiansheng.js','r',encoding='utf-8').read()).call('b',response.json())
print(ctx)