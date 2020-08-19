from scrapy_redis.spiders import RedisSpider


class BaseSpider(RedisSpider):

    def check_task(self):
        """
        查询库中有多少待爬门店及条码数据
        """
        pass