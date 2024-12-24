conda create -n myscrapy python==3.6.4#1.虚拟环境
#2.sublime设置python环境： Sublime里点击菜单栏的 Tools > Build System > New Build System，输入以下内容（python地址使用where python可以查到），然后保存文件。
{
    "cmd": ["/path/to/your/conda/envs/your_env_name/bin/python", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python"
}
Tools > Build System，然后选择刚刚创建的 Build System，运行程序（ctrl+b）,字体放大/缩小（trl++/ctrl+-）
#3.python基础知识点：
数据类型（7）：（type（var）查看类型）
布尔，（逻辑运算：and,or,not）
数字，（int，float，complex）（算数运算：+加-减*乘/除**指数运算%除取余//除取整）（比较运算：）
字符串，索引取值（str[num]）,取长度（len(str)）,str.lower()小写,str.upper()大写,str.fund("x")x的第一个下标值,str.replace("old","new")替换,str.count("x"),str.isalpha()全字母,str.isdigit()全数字
元组，
字典，dict.clear()字典清空，
集合，（&交集，|并集，-差集，^对称差集）
列表，索引取值（list[num]）,取长度（len(list)），list.append(str)追加，del list[index]删除，list.pop()返回最后一个元素，str in list判断是否存在某值，list.count(str)str存在几次，list.index(str)str存在的一个索引值
可变对象：引用赋值，如果要实现值赋值，使用copy(对象)，列表（list），字典（dict），集合（set），自定义对象
不可变对象：值赋值，整数（int），浮点数（float），字符串（str），元组（tuple），布尔值（bool）
while，continue，break，pass
for ，in，range（类型是range不是list），enumerate
函数def，return，global
类class，__init__,self（类的方法必带参数self，表示对象方法），
#4.爬虫（4类）（全网爬虫，主题爬虫，增量式爬虫，深层网络爬虫）
请求服务urllib内置，requests（pip安装）
解析页面beautifulSoup（pip install bs4），lxml(pip)，pyquery
君子协议：网站/robots.txt
策略：深度优先，广度优先，聚焦爬虫
反爬虫：headers中添加user-agent与referer；控制请求网站的速度，或者是建立IP代理池；模拟Ajax，获得所需数据；slelenium触发网页的js，模拟人类行为；
#5.实习僧：pip install requests bs4 lxml（first.py）
#6.scrapy（5部分：Engine，Scheduler,Downloader,Spiders,Item Pipeline）
安装 pip install scrapy(包含lxml pyOpenSSL twisted pywin32)
class. id# 子孙辈空格 子辈>
#7.笑话大全（second_laugh.py)
#8.scrapy入门(quotes)
创建工程：scrapy startproject tutorial
创建蜘蛛：cd tutorial
    scrapy genspider quotes quotes.toscrape.com
蜘蛛爬取：scrapy crawl quotes
python解释页面（scrapy支持css，xpath解析）：scrapy shell "http://quotes.toscrape.com/page/1/"
使用response解析内容：(css解析)response.css("title::text").extract();返回列表
（xpath解析）response.xpath("//head/title/text()").extract()（当前节点/ 当前节点以下的任意深度// 提取文本text() 根据class提取[@class='']）
#9.scrapy爬取网易新闻
scrapy startproject news
cd news
scrapy genspider -t crawl news163 news.163.com
scrapy crawl news163
items.py里面定义要爬取的数据,然后在news163.py里面爬取数据存到items里，最后在pipelines里面把items里面存的数据落盘（csv）<ITEM_PIPELINES要在settings里面开启>
#10.selenium
pip install selenium pyquery(https://googlechromelabs.github.io/chrome-for-testing/下载符合自己chrome的chromedriver)
taobao.py
爬取淘宝页面的时候，必须登录才能访问，解决办法如下： 
import time 打开页面后time.sleep(5)这期间登录
###########基础
pip install builtwith(查看网站技术栈)
fiddler(c#编写)<clear,help>
requests(pip install requests)