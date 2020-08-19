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

# jd image
# jd_image_path = '/usr/local/wcc_projects/jd_api/image'
jd_image_path = '/Users/wcc/projects/crawler/spider/spiders'

# 获取推广商品详细信息
jd_info_method = 'jingdong.service.promotion.goodsInfo'

jd_stid = 153
jd_brid = 29

# suning
suning_domain = "open.suning.com"
suning_appKey = "6c84c582f917e3f36fc372fe9cdad1e7"
suning_appSecret = "f7b9058df322de327900640998d278d5"
suning_adbookid = '129271'

suning_stid = 10145
suning_brid = 2283

# amazon
amazon_index_url = "https://assoc-datafeeds-cn.amazon.com/datafeed/listFeeds?format=text/xml"
amazon_part_url = "https://assoc-datafeeds-cn.amazon.com/datafeed/getFeed?filename="
amazon_user = 'wcc-23'
amazon_pwd = 'wcc2012'
amazon_save_dir = '/usr/local/importdata/source_file/amazon'
# amazon_save_dir = '/Users/wcc/projects/crawler/amazon_data'

amazon_stid = 448
amazon_brid = 188
AMAZON_ACCESS_KEY = 'AKIARCCT47PDNVXGUREP'
AMAZON_SECRET_KEY = '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'
AMAZON_ASSOC_TAG = 'wccmobile23-23'


# proxies
# http代理接入服务器地址端口
proxyHost = "http-proxy-t1.dobel.cn"
proxyPort = 9180

# 账号密码
proxyUser = "PANTHERHDE3S3KS0"
proxyPass = "oAaSomk5"

# proxies = {"http": f"http://{proxyUser}:{proxyPass}@{proxyHost}:{proxyPort}"}
proxy_url = f"{proxyUser}:{proxyPass}@{proxyHost}:{proxyPort}"
proxies = {"http": f"http://{proxy_url}"}