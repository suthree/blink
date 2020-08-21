from scrapy_redis.spiders import RedisSpider
import requests
import scrapy
from .constants import proxies
from fake_useragent import UserAgent
ua = UserAgent()
class BaseSpider(scrapy.Spider):
    def get_result(self, method, url, kwargs):
        headers = kwargs.get("headers")
        if headers:
            headers["User-Agent"] = ua.random
        else:
            headers = {"User-Agent": ua.random}
        response = requests.request(method, url, proxies=proxies, **kwargs)
        try:
            result = response.json()
        except Exception:
            result = response.text()
        return result

    def check_task(self):
        """
        查询库中有多少待爬门店及条码数据
        """
        pass


    def get_code_map(self):
        """
        映射关系，redis存储
        """        
        pass

    

class MallSpider(BaseSpider):
    """
    商品爬虫基类

    Args:
        BaseSpider ([type]): [description]
    """    
    pass

class SmgSpider(BaseSpider):
    """
    扫码购商品基类

    Args:
        BaseSpider ([type]): [description]
    """
    def __init__(self):
        need_map = False
        map_type = 'name' or 'barcode'
        brand = 1

    pass