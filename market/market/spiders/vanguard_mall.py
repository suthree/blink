import json

import scrapy

from ..items import MarketItem
from .base import MallSpider


class VanguardMallSpider(scrapy.Spider):
    name = 'vanguard_mall'
    allowed_domains = ['crv.com']
    start_urls = ['http://app.crv.com.cn/']
    base_url = "https://app.crv.com.cn/app_api/v1/dc-app-api/mobile/api"
    cate_url = f"{base_url}/category/list"
    product_url = f"{base_url}/product/search"
    page_size = 10
    # headers = {
        # "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 MicroMessenger/7.0.8(0x17000820) NetType/WIFI Language/zh_CN miniProgram",
        # "userId": "783449",
        # "userSession": "AB443F511CDAD94E74542B34B01A9874",
        # "channel": "weapp",
        # "appVersion": "2.9.6",
        # "Origin": "https://appres.crv.com.cn",
        # "os": "weixin_mini",
        # "subsiteId": "252",
        # "Accept-Language": "zh-cn",
        # "osVersion": "11.4",
        # "unique": "custom-2020042716521056348824622903507453042",
        # "Accept": "application/json, text/plain, */*",
        # "appkey": "ef1fc57c13007e33",
    # }

    def start_requests(self):
        # stores = self.get_task()
        stores = ['29']
        params = {"id": 1, "depth": 1, "targetCategoryIds": "all"}
        cate_url = self.cate_url + f"?param={json.dumps(params)}"
        for store_id in stores:
            kwargs = {
                'headers': {"subsiteId": str(store_id)},
                'meta': {"store_id": store_id}
            }
            yield scrapy.Request(cate_url, self.get_cates, **kwargs)
      
    def get_cates(self, response):
        result = json.loads(response.text)
        store_id = response.meta['store_id']
        if result.get("stateCode") != 0:
            return
        data = result.get("data", [])
        for item in data[:1]:
            # cat1_id = item.get("id")
            cat1_name = item.get("name")
            childs = item.get("subCategories", [])
            for child in childs:
                cat2_id = child.get("id")
                cat2_name = child.get("name")
                cate_name = "_".join([cat1_name, cat2_name])
                print(cate_name)
                page = 1
                param = {
                    "virtualCategoryId": [cat2_id],
                    "order": 0,
                    "page": page,
                    "pageCount": self.page_size,
                    # "stock": stock,
                }
                kwargs = {
                    'headers': {
                        "subsiteId": str(store_id),
                        # "Content-Type": "application/x-www-form-urlencoded",
                        'Content-Type': 'application/json'
                    },
                    'meta': {
                        "page": page,
                        "cat_id": cat2_id,
                        "cat_name": cate_name,
                        "store_id": store_id,
                    },
                    'method': "POST",
                    # "data": f"param={json.dumps(param)}",
                    # "body": json.dumps({'param': param})
                    # "body":  f"param={json.dumps(param)}"
                    # "body":  json.dumps(param)
                    "param": param
                }
                yield scrapy.Request(
                    self.product_url,
                    self.parse_products,
                    **kwargs,
                )
                # self.get_products(store_id, cat2_id, cate_name)

    def get_products(self, store_id, cat_id, cate_name, page=1, stock=1):
        param = {
            "virtualCategoryId": [cat_id],
            "order": 0,
            "page": page,
            "pageCount": self.page_size,
            # "stock": stock,
        }
        kwargs = {
            'headers': {
                "subsiteId": str(store_id),
                "Content-Type": "application/x-www-form-urlencoded",
            },
            'meta': {
                "page": page,
                "cat_id": cat_id,
                "cat_name": cat_name,
                "store_id": store_id,
            },
            'method': "POST",
            "data": f"param={json.dumps(param)}",
        }
        yield scrapy.Request(
            self.product_url,
            self.parse_products,
            **kwargs,
        )

    def parse_products(self, response):
        result = json.loads(response.text)
        print(result)
        if result.get("stateCode") != 0:
            return 0
        meta = response.meta
        cat_name = meta['cat_name']
        page = meta['page']

        products = result.get("data", {}).get("items", [])
        total_count = result.get("data", {}).get("total", 0)
        for item in products:
            brand = item.get("brand")
            goods_id = item.get("defaultGoodsId")
            pro_id = item.get("id")
            details = item.get("goodsMVO", {})
            # pro_details = details.get('popDetailss', [{}])
            # pro_type = pro_details.get('popPolicyMemo')
            # start_date = pro_details.get('staDate')
            # end_date = pro_details.get('endDate')

            pro_details2 = details.get("promotionPriceVO", {})
            product_id = details.get("spuCode")
            sys_codes = dict(goods_id=goods_id, product_id=product_id, id=pro_id)

            # on_sale = item.get("offShelve")
            promotions = item.get("promotionList")
            sales = item.get("salesCount")

            prices = item.get("flashSale", {})
            price = prices.get("price")
            price_orig = prices.get("originalPrice")

            detail = item.get("goodsMVO", {})
            spec = detail.get("weight")
            product_info = MarketItem()
            product_info = dict(
                product_id=product_id,
                product_name=item.get("name"),
                image_url=item.get("pic"),
                price=price,
                price_orig=price_orig,
                category=cat_name,
                brand=brand,
                unit=spec,
                sales=sales,
                on_sale=bool(promotions),
                promotion_details=str(pro_details2),
                sys_codes=str(sys_codes),
            )
            print(product_info)
            yield product_info

        if total_count > page * self.page_size:
            meta['page'] = page + 1
            self.get_products(**meta)
