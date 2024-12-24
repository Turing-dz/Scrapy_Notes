import scrapy


# class SpecialOffersSpider(scrapy.Spider):
#     name = "special_offers"
#     allowed_domains = ["www.tiny-deals.com"]
#     start_urls = ["https://www.tiny-deals.com/"]

#     def parse(self, response):
#         for product in response.xpath("//div[@class='ut2-gl__body content-on-hover']/div[@class='ut2-gl__content content-on-hover']"):
#             yield {
#                 'title':product.xpath(".//div[@class='ut2-gl__name']/a[@class='product-title']/text()").get(),
#                 'url':product.xpath(".//div[@class='ut2-gl__name']/a[@class='product-title']/@href").get(),
#                 'original_price':product.xpath(".//div[@class='ut2-gl__mix-price-and-button qty-wrap']/div/div/span/span[@class='ty-list-price ty-nowrap']/span/bdi/span[2]/text()").get(),
#                 'discounted_price':product.xpath(".//div[@class='ut2-gl__mix-price-and-button qty-wrap']/div/div/span/span[@class='ty-price']/bdi/span[@class='ty-price-num'][2]/text()").get(),
#             }
        # show_more=response.xpath("//span[@class='ty-btn ty-btn__secondary ty-ab-load-more-btn'][1]")
        # if show_more:
        #     show_more.click()
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
