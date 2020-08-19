# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# import json

# from spider import models
# from datetime import datetime
# from scrapy import signals, exceptions
# from kafka import KafkaProducer

class MarketPipeline:
    def process_item(self, item, spider):
        return item



# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.


# class PostgreSQLPipeline(object):
#     def __init__(self, schema):
#         self.session = models.create_session()
#         self.session.execute(f"SET search_path TO {schema};")
#         self._create_table()

#     @classmethod
#     def from_crawler(cls, crawler):
#         schema = crawler.settings.get('POSTGRESQL_SCHEMA')
#         return cls(schema)

#     def _create_table(self):
#         sql = datetime.now().strftime("SELECT create_month_table('%Y_%m')")
#         self.session.execute(sql)
#         self.session.commit()
#         self.session.close()

#     def process_item(self, item, spider):
#         # drop the item with illegal barcode and blank name.
#         # if not item.get('name'):
#         # not item.get('barcode', 'N').isdigit():
#         # raise exceptions.DropItem
#         crawldata = models.Crawldata(
#             wid=spider.wid,
#             logid=spider.logid,
#             stid=spider.stid,
#             currency=spider.currency,
#             currency_id=spider.currency_id)
#         sql_crawldata = models.map_orm_item(
#             scrapy_item=item, sql_item=crawldata)
#         try:
#             self.session.add(sql_crawldata)
#             # self.session.save_or_update(sql_crawldata)
#             self.session.commit()
#         except Exception as e:
#             self.session.rollback()
#             spider.logger.error(e)
#         finally:
#             self.session.close()
#             return item


# class KafkaPipeline(object):
#     def __init__(self, brokers, topic):
#         self.item_topic = topic
#         self.producer = KafkaProducer(
#             bootstrap_servers=brokers,
#             value_serializer=lambda v: json.dumps(v).encode('utf-8'),
#             retries=3,
#         )

#     @classmethod
#     def from_crawler(cls, crawler):
#         # 不同爬虫入不同的库 debug 模式开启, 入测试库, 否则 入主库
#         if crawler.spider.debug:
#             brokers = crawler.settings.get('DEV_KAFKA_BROKERS')
#             topic = crawler.settings.get('DEV_KAFKA_ITEM_TOPIC')
#         elif crawler.spider.debug is False:
#             brokers = crawler.settings.get('KAFKA_BROKERS')
#             topic = crawler.settings.get('KAFKA_ITEM_TOPIC')
#         return cls(brokers, topic)

#     @staticmethod
#     def _on_send_error(excp):
#         log.error('kafka erroe: ', excp)

#     def _send(self, topic, msg):
#         self.producer.send(topic, msg).add_errback(self._on_send_error)

#     def _shutdown(self):
#         self.producer.flush()
#         self.producer.close()

#     def process_item(self, item, spider):
#         # drop the item with illegal barcode and blank name.
#         # if not item.get('name'):
#         # not item.get('barcode', 'N').isdigit():
#         # raise exceptions.DropItem()
#         date_today = datetime.today().strftime('%Y-%m-%d')
#         # 构造标准 数据 字典, 导入kafka
#         crawldata = dict(
#             brid=spider.brid,  # 我查查商超系统 id
#             stid=spider.stid,  # 我查查门店 id
#             date_key=item.get('date_key', date_today),  # 数据日期(价格/品名)
#             # 数据入库类型: 1:只入库价格 2:只入库品名 3:入库价格和品名 4:入搜索库
#             import_type=spider.import_type,
#             barcode=item.get('barcode', None),  # 条码
#             skuid=item.get('skuid', None),  # 第三方内部编码
#             brand=item.get('brand', None),  # 品牌
#             name_orig=item.get('name_orig', None),  # 原始品名
#             name=item.get('name', None),  # 入库品名
#             spec=item.get('spec', None),  # 规格
#             unit=item.get('unit', None),  # 单位
#             stock=item.get('stock', 1),  # 库存： 0：无库存 1：有库存 2：其它
#             price_orig=item.get('price_orig', None),  # 原价
#             price_list=item.get('price_list', None),  # 标签价
#             price_sale=item.get('price_sale', None),  # 销售价格
#             currency_orig=spider.currency,  # 货币 iso 代码
#             product_url=item.get('product_url', None),  # 商品链接
#             image_url=item.get('image_url', {}),  # 商品图片
#             seller_system=item.get('seller_system', None),  # 商超子系统
#             country_code=item.get('country_code', None),  # 条码国家码
#             sale=item.get('sale', 0),  # 促销标志 1=促销 0 =非促销 >3 促销的类型
#             sale_info=item.get('sale_info', None),  # 促销描述
#             start_date=item.get('start_date', None),  # 促销开始日期
#             end_date=item.get('end_date', None),  # 促销结束日期
#             category_path=item.get('category_path', None),  # 第三方分类 path
#             category_id=item.get('category_id', None),  # 第三方分类编号
#             cat_id=item.get('cat_id', 0),  # 我查查分类 id
#             price_change_date=item.get('price_change_date', None),  # 变价日期
#             opt_time=item.get('opt_time', None),  # 操作时间
#             spare_field=item.get('spare_field', None),  # 额外字段
#         )
#         # print(crawldata)
#         self._send(self.item_topic, crawldata)

#     def close_spider(self, spider):
#         self._shutdown()
