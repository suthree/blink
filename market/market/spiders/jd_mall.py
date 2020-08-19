# -*- coding: utf-8 -*-
import hashlib
import json
from collections import OrderedDict
from datetime import datetime

import scrapy

from .base import MallSpider

# jd 接口调用常量
jd_token = "0c86f69a78b0477999f069810a787b8fmy2o"
jd_appkey = "6DAFA31DDD8E1EADAA30D1BC2D06C38D"
jd_appSecret = "478dfbd0a1f8447cb67cb6b16c333b0f"
jd_version = "2.0"
jd_api_url = "https://api.jd.com/routerjson?"

# jingdong.service.promotion.goodsInfo  获取促销商品信息价格, 最多100条
# jd_price
jd_price_method = "jingdong.ware.p.price.get"

# jd_name
jd_name_method = "jingdong.service.promotion.batch.getcode"
jd_name_webid = "669696883"
jd_name_union_id = "1000148403"
jd_name_channel = "WL"

# 获取推广商品详细信息
jd_info_method = 'jingdong.service.promotion.goodsInfo'


def jd_signature(sku_json, method):
    """
    构建 符合京东 校验的 签名
    """
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 所有请求参数都 有序字典
    params = OrderedDict([('v', jd_version), ('method', method),
                          ('app_key', jd_appkey), ('access_token', jd_token),
                          ('360buy_param_json', sku_json),
                          ('timestamp', time_stamp)])
    # 将所有参数 拼成请求字符串
    params_str = ''.join([f'{k}={v}&' for k, v in params.items()])
    # 时间戳和密钥
    sign_key = f'{jd_appSecret}timestamp{time_stamp}'
    # md5 加密
    params_query = f'{sign_key}{jd_appSecret}'
    m = hashlib.md5()
    m.update(params_query.encode('utf-8'))
    sign = m.hexdigest().upper()
    return sign, params_str

class JdMallSpider(MallSpider):
    """
    京东商品 增量获取
    """
    name = 'jd_mall'
    allowed_domains = ['www.jd.com']
    start_urls = ['https://search.jd.com']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skus = []
        self.range = 10  # 每个分类取300条分类, 300/30 = 10

    def start_requests(self):
        cat_path = '1320,1585,9434'  # 饮料，牛奶饮品
        page = 1
        pro_url = f'https://list.jd.com/list.html?cat={cat_path}&page={page}&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main'
        yield scrapy.Request(pro_url, self.get_product)

    def get_url(self, sku):
        params = {
            "url": f"http://item.jd.com/{sku}.html",
            "unionId": jd_name_union_id,
            "channel": jd_name_channel,
            "webId": jd_name_webid
        }
        sign, params_str = jd_signature(params, jd_name_method)
        name_url = f'{jd_api_url}{params_str}sign={sign}'
        yield scrapy.Request(name_url, self.parse_items)

    def parse_url_items(self, response):
        """
        {
            "jingdong_service_promotion_batch_getcode_responce": {
                "code": "0",
                "querybatch_result": "{\"resultCode\":\"0\",\"resultMessage\":\"获取代码成功\",\"urlList\":[{\"id\":0,\"url\":\"https://union-click.jd.com/jdc?e=&p=AyIHZRprFQQWBFQfUiVGTV8LRGtMR1dGXgVFTUdGW0pADgpQTFtLG10RARMDXAQCUF5PNz1vAnReS2MzfhgPYRFcJ2YDXlpUYAMXVyUFFQ9SE1wcCxA3VRpaFAIXDlAaWSUyEgZlTTUVAxMGVBteEAoTN1QrWxEGEgdSG1wXARYDUStcJdWrp4K1z8KshtHZu42/rCI3ZStrJQIiBGVEH0hfIgY=&t=W1dCFBBFC1pXUwkEAEAdQFkJBVsTBhEGURJETEdOWg==\"}]}"
            }
        }
        """
        result = response.json()
        res_json  = result.get('jingdong_service_promotion_batch_getcode_responce', {}).get('querybatch_result', [])
        urls = json.loads(res_json)
        url_list = urls.get('urlList', [])
        for item in url_list:
            app_url = item['url']


    def get_price(self, sku):
        """
        构造price 接口参数，支持多个skuid 一起查询，最多10个

        Args:
            sku ([type]): [description]

        Yields:
            [type]: [description]
        """        
        skuids = [f'J_{sku}']
        params = dict(skuids=','.join(skuids), area='1')
        sign, params_str = jd_signature(params, jd_price_method)
        price_url = f'{jd_api_url}{params_str}sign={sign}'
        # sku_infos = {f'J_{sku}': sku}
        yield scrapy.Request(price_url, self.parse_price_items)


    def parse_price_items(self, response):
        """
        {
            "jingdong_ware_p_price_get_responce": {
                "code": "0",
                "skuPriceList": [
                    {
                        "id": "J_1978183",
                        "m": "9.80",
                        "op": "8.80",
                        "p": "8.80"
                    }
                ]
            }
        }
        """
        res = response.json()
        products = res.get('jingdong_ware_p_price_get_responce', {}).get('skuPriceList', [])
        sku_info_dict = response.meta['sku_info']
        for pro in products:
            skuid, name, barcode, cbrand, item_url, image_path, app_url = sku_info_dict[
                pro['id']]
            # 价格为-1, 无库存, 不入数据库, app_url 无值, 置为空
            price = pro['p']
            if price != '-1.00':
                product = dict(skuid=skuid,
                               brand=cbrand,
                               name_orig=name,
                               barcode=barcode,
                               price_sale=price,
                               product_url=app_url or None,
                               image_url={'main': image_path})
                yield product


    def get_product(self, response):
        skus = response.xpath("//@data-sku").extract()
        for skuid in set(skus):
            if skuid not in self.skus:
                # 通过列表作一层判断, 不需要经过数据库,作on conflict
                self.skus.append(skuid)
                base_url = 'https://api.jd.com/routerjson?v=2.0&method=jingdong.new.ware.baseproduct.get&app_key=6DAFA31DDD8E1EADAA30D1BC2D06C38D&access_token=1b64f051-0122-478c-b3dc-46c814c1b8aa&360buy_param_json={"ids":"'
                end_url = '","basefields":"valuePayFirst,skuId,saleUnit,model,phone,weight,issn,wserve,imagePath,skuMark,state,shopCategorys,brandId,isDelete,allnum,height,name,valueWeight, length,barCode,saleDate,safeDays,erpPid,cbrand,site,sizeSequence,productArea,packSpecification,width,cid2,maxPurchQty,ebrand,upc,url,size,category,venderType, color,shopName,pname,colorSequence"}&timestamp=2019-06-11 13:19:30&sign=0324D043DF6D3605E74C07820B8FDAF1'
                product_url = base_url + str(skuid) + end_url
                yield scrapy.Request(product_url, self.parse_product_items)


    def parse_product_items(self, response):
        product_list = response.json()['jingdong_new_ware_baseproduct_get_responce'][
                'listproductbase_result']
        products = [(pro["skuId"], pro["name"], int(pro.get("isDelete", "-1")),
                     pro.get("state", ""), pro.get("barCode", ""),
                     pro.get("erpPid", "-1"), pro.get("color", ""),
                     int(pro.get("colorSequence", "-1")), pro.get("size", ""),
                     int(pro.get("sizeSequence", "-1")), pro.get("upc", "-1"),
                     pro.get("skuMark", ""), pro.get("saleDate", ""),
                     int(pro.get("cid2", "-1")),
                     float(pro.get("valueWeight", "0.00")),
                     float(pro.get("weight", "0.00")),
                     pro.get("productArea", ""), pro.get("wserve", ""),
                     pro.get("allnum", ""), int(pro.get("maxPurchQty", "-1")),
                     pro.get("brandId", "-1"), pro.get("valuePayFirst", ""),
                     float(pro.get("length", "0.00")),
                     float(pro.get("width", "0.00")),
                     float(pro.get("height", "0.00")), pro.get(
                         "venderType", ""), pro["pname"],
                     int(pro.get("issn", "-1")), int(
                         pro.get("safeDays", "-1")), pro.get("saleUnit", ""),
                     pro.get("packSpecification", ""), pro.get("category", ""),
                     pro.get("shopCategorys", ""), pro.get("phone", ""),
                     pro.get("site", ""), pro.get("ebrand", ""),
                     pro.get("cbrand", ""), pro.get("model", ""),
                     pro.get("imagePath", ""), str(pro.get("shopName", "")),
                     pro.get("url", ""), 'now()') for pro in product_list]
