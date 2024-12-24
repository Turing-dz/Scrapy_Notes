import requests
import execjs#pip install pyexecjs2
cookies = {
    'acw_tc': '1a0c652117333673251408215e0100f9fedc0a7a3834dfd88e3428caecbadb',
    'Hm_lvt_b966fe201514832da03dcf6cbf25b8a2': '1733367326',
    'HMACCOUNT': '43D7FCC8A4C6643B',
    'Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2': '1733367793',
    'ssxmod_itna': 'YqjOAKBIeRxGhBDz=DUBfqoYIe7Ki+PIhxDCDAhwGhqGX6qoDZDiqAPGhDCbSKcnmxtiBB0xH5CBhRhY0ihRxj7zG=AhLET74B3DEx0=N8QoxiiMDCeDIDWeDiDGRtDFxYoDe1VQDFGkvzlxv8DWKDKx0kDY5DwaYhDiPD7xyKeAnCtDDztBEqkCYqkDi30pyHdF7wDiv5g62K0xG1DQ5Ds106tD5D0hLUtlHzXKdEUAF+o40OD0KmyPFwaQHGM1KEWG+dqA+iIhnKzjhoQYp5eAbxdBx31jhKXN/xIn63kY2eBMDDi6xAbBz4D=',
    'ssxmod_itna2': 'YqjOAKBIeRxGhBDz=DUBfqoYIe7Ki+PIhxDCDAhwGxA69+WD/i9DFOudg0KoxpGQD6jxp=N5q3l0Gm5ZQnu=NtztCicC51QCTu=aZQ7YNwzicPyrTEo8wr489eFBBB=yebG5aOkBoW4e7vsIQyxYx+QGCYsw=i4ughw/OerK3Isghg7rUehKbyrkjArBOczZeE+Y+qq9GbC578+mt0=IxpH51e8P2ksM9WIle97YOjs9mP3icmkP1DkNkKEghe3Cpck7o5vRl37e/LBOU2LlOMGlxau9j3ENjjaollKqb4q1Z3rI2P1FfqFhYD8H2fdxCiT33urd33NVgY22=ZkW6gk4xoeoO42bjkYxmis3QmSbuO7ixGDkQ1lKL+pz7iThpXfFQC3iE79GDIAzRGP=mbB2TqYHd8qh+DYEvH2K3D5Y3FjOwD3Ir35CODlqxFxE=C3m3mv2NYrGZhrV0+IRxbE5YGDpm3Kr890ejCDpaIVrkuEImf3x+iG0wA0iIGDPt3P1zwptv3QVd5q4TTlDhkaAhtaOaEWLXTmC=1robXQ3y7H3f+pwp+MWbEdKfeqlFUc+nEjIgDHgnoSUsoQT6I+m5s2dQnQSTWsQw0bmucg=NT+fy6DDw1KqBvjBDBjTHqmMC8U5oBRk1dtGFeKeMbBxTC/kmzWjzCWDDjKDeux4D===',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'acw_tc=1a0c652117333673251408215e0100f9fedc0a7a3834dfd88e3428caecbadb; Hm_lvt_b966fe201514832da03dcf6cbf25b8a2=1733367326; HMACCOUNT=43D7FCC8A4C6643B; Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2=1733367793; ssxmod_itna=YqjOAKBIeRxGhBDz=DUBfqoYIe7Ki+PIhxDCDAhwGhqGX6qoDZDiqAPGhDCbSKcnmxtiBB0xH5CBhRhY0ihRxj7zG=AhLET74B3DEx0=N8QoxiiMDCeDIDWeDiDGRtDFxYoDe1VQDFGkvzlxv8DWKDKx0kDY5DwaYhDiPD7xyKeAnCtDDztBEqkCYqkDi30pyHdF7wDiv5g62K0xG1DQ5Ds106tD5D0hLUtlHzXKdEUAF+o40OD0KmyPFwaQHGM1KEWG+dqA+iIhnKzjhoQYp5eAbxdBx31jhKXN/xIn63kY2eBMDDi6xAbBz4D=; ssxmod_itna2=YqjOAKBIeRxGhBDz=DUBfqoYIe7Ki+PIhxDCDAhwGxA69+WD/i9DFOudg0KoxpGQD6jxp=N5q3l0Gm5ZQnu=NtztCicC51QCTu=aZQ7YNwzicPyrTEo8wr489eFBBB=yebG5aOkBoW4e7vsIQyxYx+QGCYsw=i4ughw/OerK3Isghg7rUehKbyrkjArBOczZeE+Y+qq9GbC578+mt0=IxpH51e8P2ksM9WIle97YOjs9mP3icmkP1DkNkKEghe3Cpck7o5vRl37e/LBOU2LlOMGlxau9j3ENjjaollKqb4q1Z3rI2P1FfqFhYD8H2fdxCiT33urd33NVgY22=ZkW6gk4xoeoO42bjkYxmis3QmSbuO7ixGDkQ1lKL+pz7iThpXfFQC3iE79GDIAzRGP=mbB2TqYHd8qh+DYEvH2K3D5Y3FjOwD3Ir35CODlqxFxE=C3m3mv2NYrGZhrV0+IRxbE5YGDpm3Kr890ejCDpaIVrkuEImf3x+iG0wA0iIGDPt3P1zwptv3QVd5q4TTlDhkaAhtaOaEWLXTmC=1robXQ3y7H3f+pwp+MWbEdKfeqlFUc+nEjIgDHgnoSUsoQT6I+m5s2dQnQSTWsQw0bmucg=NT+fy6DDw1KqBvjBDBjTHqmMC8U5oBRk1dtGFeKeMbBxTC/kmzWjzCWDDjKDeux4D===',
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
    'type__1017': 'n4+hDKAKD5YvPQqGKG=D/tF4BKAvUCijYrCrYD',
}

response = requests.get(
    'https://ctbpsp.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/2',
    params=params,
    cookies=cookies,
    headers=headers,
)
# print(response.text)
# ctx=execjs.compile(open('./3zhaobiao.js','r',encoding='utf-8').read()).call('decryptByDES',response.text)
ctx=execjs.compile(open('./3zhaobiao.js','r',encoding='utf-8').read()).call('decryptByDES',response.json())
print(ctx)