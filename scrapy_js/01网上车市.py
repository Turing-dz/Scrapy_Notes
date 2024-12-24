import requests
import re
#1.爬取页面text
url="https://www.cheshi.com/"
response=requests.get(url)
print(response.text)
print(response.status_code)
print(response.headers)
print(response.encoding)
with open("./网上车市.html","w",encoding="utf-8") as f:
    f.write(response.text)

# 2.爬取图片content
url_image="https://icon.cheshi-img.com/bseries_coverimg/5208_300.png"
response=requests.get(url_image)
with open("./car.jpg","wb") as f:#写入2进制图片数据
    f.write(response.content)#图片用content，不是text



# 3.携带请求头获取数据
url="https://product.cheshi.com/rank/2-0-0-0-1/"
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
response=requests.get(url,headers=headers)
print(response.text)
print(response.request.headers)

# 4.提取关键数据
url="https://product.cheshi.com/rank/2-0-0-0-1/"
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
response=requests.get(url,headers=headers)
exp=re.compile('class="m_detail".*?href.*?>(.*?)<',re.S)#匹配出（）里的内容，re.S代表匹配包括换行符
print(exp.findall(response.text))#在response.text里面匹配出规则内容
for title in exp.findall(response.text):
    print(title)
    
    
#5.正则表达式
str="Hi \n _12!"
print(str)
print(re.findall(".",str))#.单个字符匹配，换行符字符删掉['H', 'i', ' ', ' ', '_', '1', '2', '!']
print(re.findall("..",str))#..连着的2个字符匹配，有换行符的删掉，不够的删掉（跨2步走,不匹配的跨1步走）['Hi', ' _', '12']
print(re.findall("...",str))#['Hi ', ' _1']
print(re.findall("....",str)) #[' _12']

print(re.findall("\w",str))#\w匹配所有的字母数字下划线['H', 'i', '_', '1', '2']
print(re.findall("\w\w",str))#['Hi', '_1']
print(re.findall("\w\w\w",str))#['_12']

print(re.findall("\W",str))#\W匹配所有 非 字母数字下划线[' ', '\n', ' ', '!']8
print(re.findall("\W\W",str))#[' \n']
print(re.findall("\W\W\W",str))#[' \n ']

print(re.findall("\d",str))#\d匹配数字['1', '2']
print(re.findall("\d\d",str))#['12']

print(re.findall("\D",str))#\D匹配 非 数字['H', 'i', ' ', '\n', ' ', '_', '!']

print(re.findall("\s",str))#\s只匹配空格和换行符[' ', '\n', ' ']
print(re.findall("\s\s",str))#[' \n']
print(re.findall("\s\s\s",str))#[' \n ']

print(re.findall("\S",str))#\S 非 空格和换行符['H', 'i', '_', '1', '2', '!']


#组合使用
print(re.findall("\s\s\w",str))#(空格或换行符，空格或换行符，字母数字下划线)['\n _']
print(re.findall("\w \s",str))#(字母数字下划线，空格，空格或换行符)['i \n']

str2="Hello World 123"
print(re.findall("e",str2))#['e']
print(re.findall("l\w",str2))#['ll', 'ld']
#[]匹配里面任意字符
print(re.findall("[abcde]",str2))#['e', 'd']
print(re.findall("[a-e]",str2))#['e', 'd']
print(re.findall("[^a-e]",str2))#除了a-e外匹配所有['H', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', ' ', '1', '2', '3']
print(re.findall("[12]",str2))#['1', '2']
print(re.findall("[12][12]",str2))#['12']
print(re.findall("[0-9]",str2))#['1', '2', '3']
print(re.findall("[0-2a-e]",str2))#['e', 'd', '1', '2']
str3="122333 abbccc"
#{}匹配重复多少次
print(re.findall("\d{3}",str3))#(数字,数字，数字）['122', '333']
print(re.findall("\w{3}",str3))#['122', '333', 'abb', 'ccc']
#*匹配重复0次或多次
print(re.findall("1*",str3))#['1', '', '', '', '', '', '', '', '', '', '', '', '', '']
print(re.findall("1*2",str3))#['12', '2']
print(re.findall("2*3",str3))#['223', '3', '3']
#+匹配重复1次或多次
print(re.findall("1+",str3))#['1']
print(re.findall("1+2",str3))#['12']
print(re.findall("\d+",str3))#['122333']

str4="X1Y22Y333Y4444"
print(re.findall("X.*Y",str4))#（X,除了\n匹配零次或多次，Y）['X1Y22Y333Y']贪婪匹配，匹配最长的
#?惰性匹配
print(re.findall("X.*?Y",str4))#['X1Y']
print(re.findall("Y.*?Y",str4))#['Y22Y']
print(re.findall("\d.*Y",str4))#['1Y22Y333Y']
print(re.findall("\d.*?Y",str4))#['1Y', '22Y', '333Y']
#预加载匹配规则
exp=re.compile("\w+")#（字母数字下划线，匹配一次或多次）
print(exp.findall(str2))#['Hello', 'World', '123'] 
#分组获取数据
str5="My name is Martian!My name is Zoe!My name is Jodie!"
exp=re.compile("is (.*?)!")
print(exp.findall(str5))#['Martian', 'Zoe', 'Jodie']
str6='''
My name is Martian,and I am 25 years old.
My name is Zoe,and I am 27 years old.
My name is Jodie,and I am 23 years old.
'''
exp=re.compile("is (.*),.*?am (\d*)")
print(exp.findall(str6))#[('Martian', '25'), ('Zoe', '27'), ('Jodie', '23')]






#xpath(pip install lxml)
from lxml import etree
url="https://product.cheshi.com/rank/2-0-0-0-1/"
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
response=requests.get(url,headers=headers)

tree=etree.HTML(response.text)
title=tree.xpath('//div[@class="m_detail"]//a/text()')
print(title)
