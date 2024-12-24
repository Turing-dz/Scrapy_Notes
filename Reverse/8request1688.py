import time
import execjs
import requests
token='536591ca3e2c109bb8fe2bd19d95b22e'
t=round(time.time()*1000)#保留13位
g='12574478'
data='{"url":"https://pjjx.1688.com/index.html?wh_pha=true&wh_pid=2207353&__existtitle__=1&tt=fwl&gad_source=1&gclid=EAIaIQobChMImfnklLaSigMV8iN7Bx3VvRJYEAAYASAAEgIG4_D_BwE&tracelog=cps&clickid=eebd0e26b9d686dac080fe1adf0086ca","params":"{\"buildPlatform\":\"pegasus\",\"pageType\":\"pc\",\"platform\":\"pc\",\"url\":\"https://pjjx.1688.com/index.html?wh_pha=true&wh_pid=2207353&__existtitle__=1&tt=fwl&gad_source=1&gclid=EAIaIQobChMImfnklLaSigMV8iN7Bx3VvRJYEAAYASAAEgIG4_D_BwE&tracelog=cps&clickid=eebd0e26b9d686dac080fe1adf0086ca\"}","isGray":false,"useHyperDataPrefetch":true}'
signKey = token + "&" + str(t) + "&" + g + "&" + data
with open('./8request1688.js',"r",encoding="utf-8") as f:
    jscode=f.read()
ctx=execjs.compile(jscode).call("h",signKey)
print(ctx)
params={
    "jsv":"2.6.1",
"appKey":'12574478',
"t":t,
"sign":ctx, 
"v":"1.0",
"type":"jsonp",
"isSec":"0",
"timeout":"20000",
"api":"mtop.alibaba.cbu.wireless.uniform.render.getpagedata",
"usePrefetch":"true",
"dataType":"jsonp",
"callback":"mtopjsonp2",
}
params["data"]=data
url="https://h5api.m.1688.com/h5/mtop.alibaba.cbu.wireless.uniform.render.getpagedata/1.0/?"
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
         "referer":"https://pjjx.1688.com/",
         "cookie":"cbu_mmid=7E3C55520E991B9B6A5DD881E253EFAFD74CBB9E79487AA7EB4A6D73D956B43309F848C1F03189F222CD52D098667A99AADB55BB6475901599CB4E3CC0105D53; ta_info=431EEA0EF470984D28D52453CC0DA41297234972A6103BDF50F0FE8F811E949D09EAF4563BC57F777E448EB059A88EB6173A6686E9536F60EB4FE6DAA637AC8FAF2CA3EE75D61A53F591632068CD27FA23353CF97B100118F6ABC7375BE99A024B1558AEE22B19377108248434DE77F8F60FAE5C9F8BC46F2CE1F4ABC539D14F24E78C062EF5EB51; mtop_partitioned_detect=1; _m_h5_tk=536591ca3e2c109bb8fe2bd19d95b22e_1733470905511; _m_h5_tk_enc=0573b84694c9ba1699622ef7497fe0ad; cna=MnvZH6OyxTQCAXj2XgJnfran; xlly_s=1; isg=BPHxrD2yMtLn9Z7GzoUnFDxTAH2L3mVQaU6xANMGi7jX-hFMGy-KIMxZHI6cMv2I; tfstk=fGqtNzbTe6fgx-9pJE_niZb9tEBhqoeap5yWmjcMlWFL352Di-g6RpMZtlcgIcsYk7PJiqZmioBxbk4MmffZD-NoD_flqg2aQcofZ_ctKcgicxsmGb6_OKmqc_fhqg2aQmPr3QK35eMITxHXGfNjAHMohmOs1SGIRYMk1mNjc9hI3YtXlFT1ApMrOjijcSwIgZXtTdM9DrYPgLkc7iOMskHCgbwTbvkUvyutN2GpcAEKBVh7Blbm8JDQxk3o-KfnA8z31vnRxFi7prN8PS7k8ceb5SuL_68Ktya3hjgBEnyKkfUQf2pXcJwEG4UY61LZ1PVKzvgBHgk3ZXwafyB2ORNo6cMI-g68dqa3b4rGOhn7zRmglS7k8ceb5DIr4uq-yqOowxY1p9L2uVMU7Am8MWpdHbkKZOg6uEumLvhlp9L2uVMEpbX6cE8qov5.."}
res=requests.get(url,headers=headers,params=params)
print(res.text)