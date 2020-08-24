

import json

from pyspider.libs.base_handler import BaseHandler


def get_range_times(count, gap):
    times, remainder = divmod(count, gap)
    if remainder > 0 and times:
        times += 2
    else:
        times = 1
    return times
    

class VanguardMallSpider(BaseHandler):
    name = 'vanguard_mall'
    allowed_domains = ['crv.com']
    start_urls = ['http://app.crv.com.cn/']
    base_url = "https://app.crv.com.cn/app_api/v1/dc-app-api/mobile/api"
    cate_url = f"{base_url}/category/list"
    product_url = f"{base_url}/product/search"
    page_size = 10

    # @every(minutes=24 * 60)
    def on_start(self):
        # stores = self.get_task()
        stores = ['29']
        for store_id in stores:
            all_cates = self.get_cates(store_id)
            for cat1_id, cat1_name, cat2_id, cat2_name in all_cates:
                cate_name = "_".join([cat1_name, cat2_name])
                total_count = self.get_products(store_id, cat2_id, cate_name)
                if total_count:
                    times = get_range_times(total_count, self.page_size)
                    for i in range(2, times):
                        self.get_products(store_id, cat2_id, cate_name, i)
    
    def get_cates(self, store_id, **kwargs):
        params = {"id": 1, "depth": 1, "targetCategoryIds": "all"}
        cate_url = self.cate_url + f"?param={json.dumps(params)}"
        kwargs = {
            'headers': {"subsiteId": str(store_id)},
            'meta': {"store_id": store_id}
        }
        return self.crawl(cate_url, kwargs, callback=self.parse_cates)

    def parse_cates(self, response):
        result = response.json()
        if result.get("stateCode") != 0:
            return
        data = result.get("data", [])
        all_cates = []
        for item in data[:1]:
            cat1_id = item.get("id")
            cat1_name = item.get("name")
            childs = item.get("subCategories", [])
            for child in childs:
                cat2_id = child.get("id")
                cat2_name = child.get("name")
                cate_info = [cat1_id, cat1_name, cat2_id, cat2_name]
                all_cates.append(cate_info)
        return all_cates
                
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
            "data": f"param={json.dumps(param)}",
            'cate_name':cate_name,
        }
        return self.crawl(self.product_url, kwargs, callback=self.parse_products)

    def parse_products(self, response):
        cate_name = response['cate_name']
        result = response.json()
        if result.get("stateCode") != 0:
            return 0
        products = result.get("data", {}).get("items", [])
        total_count = result.get("data", {}).get("total", 0)
        for item in products:
            brand = item.get("brand")
            goods_id = item.get("defaultGoodsId")
            pro_id = item.get("id")
            details = item.get("goodsMVO", {})
            pro_details = details.get("promotionPriceVO", {})
            product_id = details.get("spuCode")
            sys_codes = dict(goods_id=goods_id, id=pro_id)
            promotions = item.get("promotionList")
            sales = item.get("salesCount")

            prices = item.get("flashSale", {})
            price = prices.get("price")
            price_orig = prices.get("originalPrice")

            detail = item.get("goodsMVO", {})
            spec = detail.get("weight")
            # product_info = MarketItem()
            product_info = dict(
                product_id=product_id,
                product_name=item.get("name"),
                image_url=item.get("pic"),
                price=price,
                price_orig=price_orig,
                category=cate_name,
                brand=brand,
                unit=spec,
                sales=sales,
                on_sale=bool(promotions),
                promotion_details=str(pro_details),
                sys_codes=str(sys_codes),
            )
            print(product_info)
        return total_count
