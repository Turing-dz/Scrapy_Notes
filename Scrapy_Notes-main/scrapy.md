scrapy

安装

```python
conda create -n scrapy python
conda activate scrapy
pip install scrapy
```

测试(关闭防火墙，管理员身份打开命令提示符)

```python
scrapy #查看版本和基本命令
scrapy bench #查看电脑的爬取性能
scrapy fetch http://www.baidu.com #获取baidu页面html
```

## worldometers

创建新工程

```python
mkdir scrapy_projects
cd scrapy_projects
scrapy startproject worldometers #创建名称为 worldometers的scrapy项目
cd worldometers
scrapy genspider countries www.worldometers.info/world-population/population-by-country #生成名称为 countries的spider
```

测试scrapy shell获取元素

```python
scrapy shell
fetch("https://www.worldometers.info/world-population/population-by-country/")#fetch方法进行请求,返回的数据是response
r=scrapy.Request(url="https://www.worldometers.info/world-population/population-by-country/")#Request对象进行请求，r是Request对象
fetch(r)
response.body #拿到页面html
view(response)#在浏览器中打开这个html
title=response.xpath("//h1")#xpath方式获取元素
response.xpath("//h1/text()").get()#xpath方式获取唯一元素的文字内容
title_css=response.css("h1::text").get() #css方式获取唯一元素文字内容
response.xpath("//td/a/text()").getall()#xpath方式获取所有次元素的文字内容，返回是一个列表
response.css("td a::text").getall()#css方式获取所有次元素的文字内容，返回是一个列表
```

scrapy代码爬取数据

```python
#1.首先在生成的countriesSpider里面的parse函数里解析response里所需要的数据
def parse(self, response):
        title=response.xpath("//h1/text()").get()
        countries=response.xpath("//td/a/text()").getall()
        yield {
            "title":title,
            "countries":countries,
        }
#2.在目录的命令提示符里crawl这个spider进行数据爬取
scrapy crawl countries
```

scrapy代码爬取两层数据，并导出

```python
#1.首先访问start_urls，然后拿到返回后放在parse里面进行处理，处理的结果都放在一个调度器里面，当parse函数处理完成后，这个调度器里的任务都同时调用parse_country函数进行处理
class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]
    def parse(self, response):
        countries=response.xpath("//td/a")
        for country in countries:
            name=country.xpath(".//text()").get()
            link=country.xpath("./@href").get()
            # absolute_link=f"https://www.worldometers.info{link}"#1.字符串拼接-域名链接
            # yield scrapy.Request(url=absolute_link)
            # absolute_link=response.urljoin(link)#2.response的urljoin方法拼接-域名链接
            # yield scrapy.Request(url=absolute_link)
            # yield response.follow(url=link)# 3.response的follow方法直接访问（内部拼接-域名链接）
            yield response.follow(url=link,callback=self.parse_country,meta={'country_name':name})#对首url访问后，再follow link，并对link返回的子页面的html在parse_country函数里处理
    def parse_country(self,response):
        # logging.info(response.url)
        name=response.request.meta['country_name']#response.request.meta获取上层传递的参数
        rows=response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year=row.xpath(".//td[1]/text()").get()
            population=row.xpath("./td[2]/strong/text()").get()
            yield{
                'name':name,
                'year':year,
                'population':population
            }
#2.在目录的命令提示符里crawl这个spider进行数据爬取,并导出为自己需要的格式
scrapy crawl countries -o population_dataset.json
scrapy crawl countries -o population_dataset.csv
scrapy crawl countries -o population_dataset.xml
```

command debug

```python
scrapy parse --spider=countries -c parse_country --meta='{\"country_name\":\"China\"}'  https://www.worldometers.info/world-population/china-population/ #使用countries这个spider调用parse_country这个callback，传递参数meta，去访问这个url
```

shell debug

```python
from scrapy.shell import inspect_response
def parse_country(self,response):
        inspect_response(response, self)
scrapy crawl countries #使用cmd运行打开shell
request.headers #查看spider的headers
response.body#查看返回数据
view(response)#页面打开返回的数据
```

browser debug

```python
from scrapy.utils.response import open_in_browser
def parse_country(self,response):
         open_in_browser(response) 
scrapy crawl countries
```

logging debug

```python
import logging
def parse_country(self,response):
         logging.info(response.status)
scrapy crawl countries
```

自定义debug(在项目根目录下创建run.py)

```python
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from worldometers.spiders.countries import CountriesSpider
process = CrawlerProcess(settings=get_project_settings())
process.crawl(CountriesSpider)
process.start()#然后打断点，进行step in
```

## tinydeal

创建工程

```python
scrapy startproject tinydeal #1.创建scrapy工程
cd tinydeal
scrapy genspider special_offers www.tiny-deals.com/ #2.在工程里创建一个spider
scrapy crawl special_offers -o dataset.json #3.抓取的数据导出
scrapy shell https://www.tiny-deals.com/electronics/ #4.使用scrapy shell爬取数据
request.headers 或者response.request.headers#查看这个爬虫的headers
```

爬取数据

```python
class SpecialOffersSpider(scrapy.Spider):
    name = "special_offers"
    allowed_domains = ["www.tiny-deals.com"]
    # start_urls = ["https://www.tiny-deals.com/electronics/"]
    def start_requests(self):
        yield scrapy.Request(url="https://www.tiny-deals.com/electronics/",callback=self.parse,headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"})
    def parse(self, response):
        for product in response.xpath("//div[@class='ut2-gl__body content-on-hover']/div[@class='ut2-gl__content content-on-hover']"):
            yield {
                'title':product.xpath(".//div[@class='ut2-gl__name']/a/text()").get(),
                'url':product.xpath(".//div[@class='ut2-gl__name']/a/@href").get(),
                'original_price': (product.xpath(".//div[@class='ut2-gl__mix-price-and-button qty-wrap']/div[@class='ut2-gl__price	pr-row-mix pr-color']/div/span/span/span/bdi/span[1]/text()").get() or '') +
                  (product.xpath(".//div[@class='ut2-gl__mix-price-and-button qty-wrap']/div[@class='ut2-gl__price	pr-row-mix pr-color']/div/span/span/span/bdi/span[2]/text()").get() or '') +
                  (product.xpath(".//div[@class='ut2-gl__mix-price-and-button qty-wrap']/div[@class='ut2-gl__price	pr-row-mix pr-color']/div/span/span/span/bdi/span[2]/sup/text()").get() or ''),

                'discounted_price': (product.xpath(".//div[@class='ut2-gl__mix-price-and-button qty-wrap']/div[@class='ut2-gl__price	pr-row-mix pr-color']/div/span/span/bdi/span[1]/text()").get() or '') +
                    (product.xpath(".//div[@class='ut2-gl__mix-price-and-button qty-wrap']/div[@class='ut2-gl__price	pr-row-mix pr-color']/div/span/span/bdi/span[2]/text()").get() or '') +
                    (product.xpath(".//div[@class='ut2-gl__mix-price-and-button qty-wrap']/div[@class='ut2-gl__price	pr-row-mix pr-color']/div/span/span/bdi/span[2]/sup/text()").get() or ''),
                'User-Agent':response.request.headers['User-Agent']

            }
        next_page=response.xpath("//div[@class='ty-pagination']/a[@class='ty-pagination__item ty-pagination__btn ty-pagination__next cm-history cm-ajax ty-pagination__right-arrow']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page,callback=self.parse,headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"})

```

IMDB(crawl模板)

```python
scrapy genspider -l #查看可以生成的spider模板
scrapy startproject imdb#生成工程
cd imdb
scrapy genspider -t crawl best_movies imdb.com #生成crawl模板的spider
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'#先更改一下settings里面的user-agent
```

爬取多页数据

```python
from typing import Iterable
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = "best_movies"
    allowed_domains = ["imdb.com"]
    # start_urls = ["https://www.imdb.com/search/title/?groups=top_250&sort=user_rating"]
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/search/title/?groups=top_250&sort=user_rating',
                             headers={
                                 'User-Agent':self.user_agent
                             })
        #process_request是对请求的处理
    rules = (Rule(LinkExtractor(restrict_xpaths="//a[@class='ipc-title-link-wrapper']"), callback="parse_item", follow=True,process_request='set_user_agent'),#这里提取a的href的时候不用@href，直接就拿到了链接
             Rule(LinkExtractor(restrict_xpaths="//a[@class='ipc-chip ipc-chip--on-baseAlt']"), follow=True,process_request='set_user_agent')#这个a链接到下一页，没有callback自动使用第一个rule的规则
             )
    def set_user_agent(self,request,spider):
        request.headers['User-Agent']=self.user_agent
        return request
    def parse_item(self, response):
    #    print(response.url)
        yield {
            'title':response.xpath("//span[@class='hero__primary-text']/text()").get(),
            'year':response.xpath("(//ul[@class='ipc-inline-list ipc-inline-list--show-dividers sc-ec65ba05-2 joVhBE baseAlt']/li[@class='ipc-inline-list__item']/a[@class='ipc-link ipc-link--baseAlt ipc-link--inherit-color'])[1]/text()").get(),
            'duration':response.xpath("(//ul[@class='ipc-inline-list ipc-inline-list--show-dividers sc-ec65ba05-2 joVhBE baseAlt']/li[@class='ipc-inline-list__item'])[3]/text()").get(),
            'gener': response.xpath("//a[@class='ipc-chip ipc-chip--on-baseAlt']/span/text()").getall(),  # 使用 getall() 提取所有标签,返回列表数据
            'rating':response.xpath("(//span[@class='sc-d541859f-1 imUuxf'])[1]/text()").get(),
            'movie_url':response.url,
            'User-Agent':response.request.headers['User-Agent']
        }

```

##  duckduckgo（splash）

安装docker desktop，成功运行docker后登录，然后更换源（setting，docker engine）

```json
{
  "builder": {
    "gc": {
      "defaultKeepStorage": "20GB",
      "enabled": true
    }
  },
  "experimental": false,
  "registry-mirrors": [

    "https://docker.mirrors.ustc.edu.cn",

    "https://registry.docker-cn.com",

    "http://hub-mirror.c.163.com",

    "https://mirror.ccs.tencentyun.com"

  ]
}
```



安装启动splash,然后访问本机的8050端口

```bash
docker pull scrapinghub/splash
docker run -it -p 8050:8050 scrapinghub/splash
#如果出现端口占用情况，就查看进程关掉进程，没有进程的话就重连网络，如下
net stop winnat
net start winnat
```

启用或关闭windows功能，关闭Hyper-v,然后下载安装Dockertoolbox（和hyper-v一个功能，这里我还是用h）。

启用splash成功后就可以访问http://127.0.0.1:8050/。

```lua
function main(splash, args)
  splash.private_mode_enabled = false
	url = args.url
  assert(splash:go(url))
  assert(splash:wait(1))
  coin = assert(splash:select_all('.table-item.filter-item.sortable'))
  coin[3]:mouse_click()
  assert(splash:wait(1))
  splash:set_viewport_full()
  return splash:png()
end
```

## livecoin(scrapy-splash)

创建工程，生成spider

```bash
scrapy startproject livecion
cd livecoin
scrapy genspider coin www.livecoinwatch.com/
```

在这个虚拟环境里面安装scrapy-splash，并配置到工程的settings文件中

```python
pip install scrapy-splash
SPLASH_URL='http://127.0.0.1:8050/'
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
```

然后编写爬虫

```python
from typing import Iterable
import scrapy
from scrapy_splash import SplashRequest

class CoinSpider(scrapy.Spider):
    name = "coin"
    allowed_domains = ["www.livecoinwatch.com"]
    # start_urls = ["https://www.livecoinwatch.com/"]
    script='''
    function main(splash, args)
        splash.private_mode_enabled = false
        url = args.url
        assert(splash:go(url))
        assert(splash:wait(1))
        coin = assert(splash:select_all('.table-item.filter-item.sortable'))
        coin[3]:mouse_click()
        assert(splash:wait(1))
        splash:set_viewport_full()
        return splash:html()
    end
    '''
    def start_requests(self):
        yield SplashRequest(url='',callable=self.parse,endpoint="execute",args={'lua_source':self.script})
    def parse(self, response):
        print(response.body)
```



最后运行爬虫

```bash
scrapy crawl coin
```

##  livecoin(selenium)

首先安装适合自己chrome版本的selenium驱动，然后再在conda环境里安装selenium包

```bash
pip install --force-reinstall -v "selenium==4.8.0" #这里必须是4.8.0,不然后面会有兼容性问题
```

爬数据

```python
from shutil import which
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import scrapy 
class CoinSpiderSelenium(Spider):
    name = "coin_selenium"
    allowed_domains = ["livecoinwatch.com"]
    start_urls = ["https://www.livecoinwatch.com/"]

    def __init__(self):  # 初始化 Selenium 驱动
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # 使用无头模式
        driver_path = which("chromedriver")
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.set_window_size(1920, 1080)

    def start_requests(self):
        # 打开页面并点击相应的元素
        self.driver.get("https://www.livecoinwatch.com/")
        coin = self.driver.find_elements(By.CLASS_NAME, "position-relative")
        coin[4].click()

        # 获取页面 HTML
        html = self.driver.page_source
        
        # 使用 HtmlResponse 包装 Selenium 的 HTML 并传递给 parse 函数
        response = HtmlResponse(url=self.start_urls[0], body=html, encoding='utf-8')
        
        # 返回一个生成器对象，这里使用 yield
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse_page, dont_filter=True, body=html, encoding='utf-8')

    def parse_page(self, response):
        self.logger.info(f"Parsing page: {response.url}")
        
        # 使用 Scrapy 的 Selector 来解析 Selenium 获取到的 HTML
        rows = Selector(response=response).xpath("//tr[contains(@class,'table-row filter-row')]")
        if not rows:
            self.logger.warning("No rows found on page!")
        
        for row in rows:
            yield {
                'name': row.xpath(".//td[2]/a/div/div[2]/small/text()").get(),
                'price': row.xpath(".//td[3]/text()[2]").get()
            }

    def closed(self, reason):
        # 在爬虫关闭时，关闭 Selenium 驱动
        self.driver.quit()

```

## google&silckdeals(scrapy-selenium)

使用selenium可以模拟用户操作，但效率太慢，将scrapy的异步能力和selenium结合，可以将需要javascrapy运行的数据进行并发爬取

```bash
pip install scrapy-selenium #虚拟环境安装库
scrapy startproject silckdeals #创建scrapy项目
cd silkdeals
scrapy genspider example example.com#在scrapy项目中创建spider
#settings里面配置
from shutil import which
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS=['-headless']  # '--headless' if using chrome instead of firefox
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}
```

首先简单爬google数据

```python
from typing import Iterable
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
from time import sleep 
class ExampleSpider(scrapy.Spider):
    name = "example"
    def start_requests(self):
        yield SeleniumRequest(url="https://google.com",wait_time=3,screenshot=True,callback=self.parse)
    def parse(self, response):
        # img=response.meta['screenshot']
        # with open("screenshot.png",'wb') as f:
        #     f.write(img)
        driver=response.meta['driver']#获取页面元素，首先需要driver
        search_input = driver.find_element(By.XPATH, "//textarea[@class='gLFyf']") 
        search_input.send_keys("hello world")
        search_input.send_keys(Keys.ENTER)
        # 获取点击后的response页面
        new_response=driver.page_source
        
        # 将新的页面内容传递给 Scrapy 进行解析
        response = scrapy.Selector(text=new_response)
        # driver.save_screenshot("after_filling_input.png")
        for link in response.xpath("//a[@jsname='UWckNb']"):
            yield {'URL':link.xpath(".//@href").get()}

```

```bash
scrapy crawl example -o url.json
```

爬取silckdeals数据

```bash
scrapy genspider computerdeals lickdeals.net/computer-deals/ #首先生成spider
```

写spider

```python
from typing import Iterable
import scrapy
from scrapy_selenium import SeleniumRequest

class ComputerdealsSpider(scrapy.Spider):
    name = "computerdeals"
    # allowed_domains = ["lickdeals.net"]
    # start_urls = ["https://slickdeals.net/computer-deals/"]
    def start_requests(self):
        yield SeleniumRequest(url='https://slickdeals.net/computer-deals/',wait_time=3,callback=self.parse)
    def parse(self, response):
        products=response.xpath("//ul[@class='bp-p-filterGrid_items']/li")
        for product in products:
            yield{
                'name':product.xpath("./div/a[2]/text()").get(),
                'link':'https://slickdeals.net'+product.xpath("./div/a[2]/@href").get(),
                'price':product.xpath("./div/span[@class='bp-p-dealCard_price']/text()").get(),
                'store_name':product.xpath("normalize-space(./div/span[@class='bp-c-card_subtitle']/text())").get(),
            }
        # response.xpath("//ul[@class='bp-p-filterGrid_items']/li").get().click()
```

开始crawl

```bash
scrapy crawl computerdeals -o data.json
```

## IMDB(pipeline&mongodb&sqlite)

 pipeline 是用来处理、过滤、清洗、验证、存储、或做进一步处理抓取到的数据的机制。

首先在pipeline里面写自己的处理过程，这里我是吧数据存放到mongodb了。

```bash
conda install pymongo dnspython -y
```

```python
from itemadapter import ItemAdapter
import logging
import pymongo
class ImdbPipeline:
    collection_name='best_movies'
    def open_spider(self,spider):
        self.client=pymongo.MongoClient("mongodb+srv://<zhuodeng0023>:<ng8ADhingmEQHf9m>@cluster0.bi6ki.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")#https://cloud.mongodb.com/v2/67087a8f1090800fc3238f3e#/overview
        self.db=self.client["IMDB"]
    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(item)
        return item
    def close_spider(self,spider):
        self.client.close()
#常用方法
process_item: 处理每个爬取到的数据项，决定是否修改、丢弃或保存。
open_spider: 爬虫开始时执行的初始化操作，如连接数据库、打开文件等。
close_spider: 爬虫结束时执行的清理操作，如关闭数据库连接、关闭文件等。
from_crawler: 从 Crawler 实例中获取全局配置，用于初始化 pipeline。
__init__: 用于 pipeline 的自定义初始化。
```

然后在settings里面添加上自己的pipeline，并设置他们运行优先级，数字越小优先级越高。这样当spider crawl到数据就会给pipeline去处理或存储到数据库之类。

```python
ITEM_PIPELINES = {
   "silkdeals.pipelines.SilkdealsPipeline": 300,#数字越小优先级越高zhuodeng0023，ng8ADhingmEQHf9m
}
```

把数据存放到sqlite中,pipeline数据处理，然后在setting里加上这个pipeline

```python
import sqlite3
class SqliteImdbPipeline:
    def open_spider(self,spider):
        self.connection=sqlite3.connect("imdb.db")
        self.cursor=self.connection.cursor()
        try:
            self.cursor.execute('''
                            CREATE TABLE best_movies(
                                title TEXT,
                                movie_url TEXT
                            )
                            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
           pass
    def process_item(self, item, spider):
        self.cursor.execute('''
                            INSERT INTO best_movies (title,movie_url) VALUES(?,?)
                            ''',(item.get("title"),item.get("movie_url")))
        self.connection.commit()
        return item
    def close_spider(self,spider):
        self.connection.close()  
ITEM_PIPELINES = {
   "imdb.pipelines.SqliteImdbPipeline": 300,
}        
```

## [Quotes to Scrape](http://quotes.toscrape.com/)（javascript）

首先这是一个javascrapt页面（ctrl+shift+禁用javascrapt，然后ctrl+r刷新，可以看到页面没有数据）（xhr查看这个网页发送的javascript网址，然后替换到start_urls,这样就可以拿到js请求返回的数据，然后使用json对数据进行处理）

```python
scrapy startproject demo_api#1.创建工程
cd demo_api
scrapy genspider quotes quotes.toscrape.com#创建spider
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/api/quotes?page=1"]

    def parse(self, response):
        resp=json.loads(response.body)
        quotes=resp.get("quotes")
        for quote in quotes:
            yield{
                'author':quote.get("author").get("name"),
                'tags':quote.get("tags"),
                'quote_text':quote.get("text")
            }
        has_next=resp.get("has_next")
        if has_next:
            next_page_number=resp.get("page") + 1
            yield scrapy.Request(
                url=f'http://quotes.toscrape.com/api/quotes?page={next_page_number}',
                callback=self.parse
            )
```

## [login](https://quotes.toscrape.com/login)(提交form)

```python
scrapy startproject demo_login
cd demo_login
scrapy genspider quotes_login quotes.toscrape.com/login
class QuotesLoginSpider(scrapy.Spider):
    name = "quotes_login"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/login"]

    def parse(self, response):
        csrf_token=response.xpath("//input[@name='csrf_token']/@value").get()
        yield FormRequest.from_response(response,formxpath='//form',formdata={"csrf_token":csrf_token,"username":"admin","password":"admin"},callback=self.after_login)
    def after_login(self,response):
        if response.xpath("//a[@href='/logout']/text()").get():
            print("logged in!")
```

## coinmarketcap（绕开cloudflare检测）

```python
scrapy startproject coinmarketcap
cd coinmarketcap
scrapy genspider -t crawl  coins coinsmarketcap.com
pip install scrapy_cloudflare_middleware
DOWNLOADER_MIDDLEWARES = {
    # The priority of 560 is important, because we want this middleware to kick in just before the scrapy built-in `RetryMiddleware`.
    'scrapy_cloudflare_middleware.middlewares.CloudFlareMiddleware': 560
}
DUPEFILTER_CLASS = "scrapy.dupefilters.BaseDupeFilter"
```

由于页面返回错误是429，而这个中间件默认处理的是503，所以在spider中导入`from scrapy_cloudflare_middleware.middlewares import CloudFlareMiddleware`,然后进入到CloudFlareMiddleware类里面，修改文件：

```python
response.status == 503 or response.status == 429
```

写spider并爬取数据



## Scrapyd

```
pip install scrapyd#安装
scrapyd#启动
pip install scrapyd-client#安装(pip install git+https://github.com/scrapy/scrapyd-client.git)
scrapyd-deploy default#启动

```

## Heroku

## craigslist(登录)

