import scrapy


class VanguardMallSpider(scrapy.Spider):
    name = 'vanguard_mall'
    allowed_domains = ['www.crv.com']
    start_urls = ['http://www.crv.com/']

    def parse(self, response):
        pass
