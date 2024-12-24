@[toc](Scrapy+Elasticsearch=SearchEngines)

# 1. Knowledges

## 1.Regex

**`.`**：匹配任意单个字符，除了换行符。

**`^`**：匹配字符串的开头。

**`$`**：匹配字符串的结尾。

**`*`**：匹配前一个字符 0 次或多次。

**`+`**：匹配前一个字符 1 次或多次。

**`?`**：匹配前一个字符 0 次或 1 次。（量词后加 `?` 实现非贪婪匹配）

**`[]`**：字符集，匹配方括号中的任意字符。（在方括号内部，.和*字符没有特殊含义；但-还是表示字符范围，\还是表示转义；而^位于方括号的开头，则表示取反，匹配不在这个字符类中的任何字符）

**`|`**：或运算符，表示匹配左边或右边的内容。 scrapy.cfg

**`\d`**：匹配任何数字，相当于 `[0-9]`。

**`\w`**：匹配任何字母、数字或下划线，相当于 `[A-Za-z0-9_]`。

`\W`：匹配不属于单词字符的任意字符。（比如：空格；标点符号如 `!`, `?`, `.`；特殊字符如 `@`, `#`, `$`, `&` 等）

**`\s`**：匹配空白字符（空白字符包括空格、制表符 (`\t`)、换行符 (`\n`)、回车符 (`\r`)、垂直制表符 (`\v`) 和换页符 (`\f`) 等）。

**`\S`**：匹配任何非空白字符。

**`\b`**：匹配单词的边界，如空格、标点符号。

**`{n}`**：匹配前一个字符恰好 n 次。

**`{n,}`**：匹配前一个字符至少 n 次。

**`{n,m}`**：匹配前一个字符至少 n 次，至多 m 次。

 `\` ：转义。

`()`：分组。分组匹配的结果的`group(0)` 返回整个匹配的结果，group(n)返回第n组的结果，嵌套时由外到里。

[\u4E00-\u9FA5]：匹配中文字符，它定义了一个字符范围，表示从 Unicode 编码 `\u4E00` 到 `\u9FA5` 之间的所有字符，即常见的汉字。

## 2.Scrapy框架

```bash
pip install scrapy #1.虚拟环境里安装scrapy框架
scrapy#2.查看scrapy框架的常用命令
scrapy startproject ArticleSpider#3.使用框架的startproject命令，创建了一个ArticleSpider工程
cd ArticleSpider
scrapy genspider cnblogs news.cnblogs.com#4.生成一个名字叫cnblogs的新的爬虫模板，news.cnblogs.com 是爬虫的目标域名
scrapy crawl cnblogs#5.执行cnblogs爬虫
```

为了对爬虫程序进行代码调试，在项目根目录（和scrapy.cfg同级目录下）创建main.py,将cmd命令放到vscode里面运行，便于调试。

```python
from scrapy.cmdline import execute
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","cnblogs"])#命令行执行scrapy crawl cnblogs
```



## 3.Xpath

`/`：表示从根节点开始选择元素。

`//`：表示在文档中选择符合条件的所有节点（不管其位置层级）。

`.`：当前节点。

`..`：父节点。

`@`：选择属性。

`[index]`：按索引选择（1-based），第一个匹配的元素为索引1。

`[@attribute]`：按属性选择，选择包含指定属性的元素。

`[text()='value']`：按文本内容选择。

`[contains(@attribute, 'value')]`：按属性部分匹配。

`text()`：选择节点的文本内容。

`contains()`：判断属性或文本是否包含某个子串。

`starts-with()`：判断属性或文本是否以某个子串开始。

`last()`：返回符合条件的最后一个节点。

`position()`：返回当前节点的位置（索引值）。

`count()`：返回节点个数。

`|`：并集运算符，选择多个路径的结果。

`and`：逻辑与。

`or`：逻辑或。

`child::`：子节点（默认的轴）。

`parent::`：父节点。

`ancestor::`：所有祖先节点（包括父节点）。

`descendant::`：所有后代节点（包括子节点）。

`following-sibling::`：后面的兄弟节点。

`preceding-sibling::`：前面的兄弟节点。

`*`：匹配任意元素。

`@*`：匹配任意属性。

## 4.Css选择器

## 5.requests

因为有些数据在源代码里面没有，是通过ajax请求获得的，所以这里用到了requests（pip install requests）库进行数据获取



## settings

里面设置ROBOTSTXT_OBEY = False。

打开pipelines,并设置images的下载

``` python
project_dir=os.path.dirname(os.path.abspath(__file__))
ITEM_PIPELINES = {
   "ArticleSpider.pipelines.ArticlespiderPipeline": 300,
   "scrapy.pipelines.images.ImagesPipeline":1
}
IMAGES_URLS_FIELD = "front_image_url"
IMAGES_STORE=os.path.join(project_dir,'images')
```

登录被识别是selenium，所以解决办法：1chrome60,chromedrive2.33(我没有尝试)

2.下载自己chrome版本对应的chrome drive(大概率没有完全一样的，我的chrome128.0.6613.138，下载的chrome drive 128.0.6613.137)，然后将chromedrive.exe放到chrome文件夹下，和chrome.exe同样目录下；然后关闭所有的chrome程序，在chrome目录下`chrome.exe --remote-debugging-port=9222`,就会自动打开本地chrome，查看127.0.0.1:9222/json，如果访问成功，就说明用命令行方式启动本地chrome成功；然后在代码中配置option：(我尝试失败)

````python
#chromedriver被识别，所以启用本地chrome：chrome.exe --remote-debugging-port=9222(访问127.0.0.1:9222/json,启动之前确保所有chrome都关闭了)
from selenium.webdriver.chrome.options import Options
chrome_option=Options()
chrome_option.add_argument("--disable-extensions")
chrome_option.add_experimental_option("debuggerAddress","127.0.0.1:9222")
service = Service(executable_path="C:/Program Files/Google/Chrome/Application/chromedriver.exe")
browser = webdriver.Chrome(service=service, options=chrome_option)# browser = webdriver.Chrome(service=service)
````

3.我尝试成功了

```python
from selenium.webdriver import ChromeOptions
option= ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_experimental_option('useAutomationExtension', False)
        service = Service(executable_path="C:/Program Files/Google/Chrome/Application/chromedriver.exe")
        browser = webdriver.Chrome(service=service, options=option)
        browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
            })
        """
        })
        browser.execute_cdp_cmd("Network.enable", {})
        browser.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser1"}})
```

Shell访问网址

```bash
scrapy shell -s USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36" https://www.zhihu.com/question/662008058
response.text
with open("D:/zhihu.html","wb") as f:
	f.write(response.text.encode("utf-8"))
```

cmder

```bash
scrapy genspider --list #1.查看scrapy框架生成spider的类型，一共有四种
# basic（默认）
# crawl（基于 CrawlSpider 类。，通过 rules 来定义复杂的链接提取和处理规则，适用于需要深度爬取整个网站的任务。）
# csvfeed（从 CSV 文件中读取源 URL 或数据来控制爬虫的行为。）
# xmlfeed（从 XML 文件中读取源数据来控制爬虫的行为。）
scrapy genspider -t crawl lagou www.lagou.com#2.使用crawl模板生成一个


```

# 反爬

## 1.随机切换useraget



使用`pip install fake-useragent` ,这个库维护了一系列可用的user-agent，首先在settings里面把默认的download-middleware关闭掉，并给出agent随机的类型。

```python
DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None，
}
RANDOM_UA_TYPE = "random"
```

然后在middlewares里面写自己的download-middleware（对request和response进行处理）

```python
class RandomUserAgentMiddleware(object):#随机更换user-agent
    #随机更换user-agent
    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)

        request.headers.setdefault('User-Agent', get_ua())
```

最后在settings里面加上自定义的middleware

```python
DOWNLOADER_MIDDLEWARES = {
    'ArticleSpider.middlewares.RandomUserAgentMiddlware': 543,
}
```



## 2.Ip代理池





