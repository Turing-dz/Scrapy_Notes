from typing import Iterable
import scrapy
from scrapy_splash import SplashRequest

class CoinSpider(scrapy.Spider):
    name = "coin"
    allowed_domains = ["livecoinwatch.com"]
    # start_urls = ["https://www.livecoin/watch.com/"]
    script='''
    function main(splash, args)
        splash.private_mode_enabled = false
        url = args.url
        assert(splash:go(url))
        assert(splash:wait(1))
        coin = assert(splash:select_all('.position-relative'))
        coin[4]:mouse_click()
        assert(splash:wait(1))
        splash:set_viewport_full()
        return splash:html()
    end
    '''
    def start_requests(self):
        yield SplashRequest(url='https://www.livecoinwatch.com/',callback=self.parse,endpoint="execute",args={'lua_source':self.script},dont_filter=False)
    def parse(self, response):
        rows=response.xpath("//tr[@class='table-row filter-row']")
        print(rows)
        for row in rows:
            yield {
                'name':row.xpath(".//td[2]/a/div/div[2]/small/text()").get(),
                'price':row.xpath(".//td[3]/text()[2]").get()
            }
