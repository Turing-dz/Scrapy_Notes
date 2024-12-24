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
