import scrapy
from scrapy_redis.spiders import RedisSpider


class VanguardMallSpider(RedisSpider):
    name = 'vanguard_mall'
    allowed_domains = ['*.crv.com']
    start_urls = ['http://www.crv.com/']

    def parse(self, response):
        pass
