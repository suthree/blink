# -*- coding: utf-8 -*-


# from suning.api import (ProductGetRequest, ProductQueryRequest,
#                         UnionInfomationGetRequest, UnionInfomationQueryRequest)

from .base import MallSpider

# suning
suning_domain = "open.suning.com"
suning_appKey = "6c84c582f917e3f36fc372fe9cdad1e7"
suning_appSecret = "f7b9058df322de327900640998d278d5"
suning_adbookid = '129271'

class SuningProductpider(MallSpider):
    name = 'suning_mall'
    allowed_domains = ['www.suning.com']
    start_urls = ['http://www.suning.com/']


    def parse(self, response):
        # 拿联盟商品信息
        for page in range(1, 70):
            data = self.get_product_Union(page)
            self.insert_product(data)

    def get_result(self, request):
        request.setDomainInfo(suning_domain, "80")
        request.setAppInfo(suning_appKey, suning_appSecret)
        try:
            result = request.getResponse()
            data = result['sn_responseContent']['sn_body']
        except Exception as e:
            data = dict()
        return data

    def get_product_Union(self, page, pagesize=50):
        """
        获取 苏宁 联盟 商品信息 77 * 50
        """
        request = UnionInfomationQueryRequest()
        request.adBookId = suning_adbookid
        request.pageNo = str(page)
        request.pageSize = str(pagesize)
        data = self.get_result(request)
        return data.get('queryUnionInfomation', [])

    def get_product_SkuName(self):
        request = ProductGetRequest()
        request.productCode = "133605250"
        # request.productName="耐克鞋"
        data = self.get_result(request)
        return data.get('product', [])


    def get_product_BrandCat(self, brandcode, catcode, page, pagesize=50):
        """
        cat_code = 'R0503002'
        brand_code = '0761'
        page =1 

        根据品牌 和分类 获取商品信息
        """
        request = ProductQueryRequest()
        request.brandCode = str(brandcode)
        request.categoryCode = str(catcode)
        request.pageNo = str(page)
        request.pageSize = str(pagesize)
        data = self.get_result(request)
        return data.get('product', [])

    def get_product(self, sku_id, barcode, name, app_url):
        """
        根据 skuid 获取苏宁联盟 商品信息
        """
        request = UnionInfomationGetRequest()
        data = self.get_result(request)
        if not data:
            return
        data = data['getUnionInfomation'][0]
        product = dict(
            skuid=sku_id,
            barcode=barcode,
            product_url=app_url,
            name_orig=data.get('goodsName', name),  # 取最新的品名
            price_sale=str(data.get('suningPrice')),
            image_url={'main': data['pictureUrl']})
        return product
