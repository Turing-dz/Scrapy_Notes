import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/']

    def parse(self, response):
        page=response.url.split("/")[-2]#拿到页码数
        filename='quotes-{}.html'.format(page)#文件名称拼接
        with open(filename,"w") as f:
        #     f.write(response.body)
        # self.log("saved file {}".format(filename))#保存成功说明
            quotes=response.css(".quote")
            for quote in quotes:
                title=quote.css(".text::text").extract()[0]
                author=quote.css(".author::text").extract()[0]
                tags=quote.css(".tag::text").extract()
                print("title\n{}\nauthor\n{}\ntags\n{}\n".format(title,author,tags))
                f.write("title\n{}\nauthor\n{}\ntags\n{}\n".format(title,author,tags))
