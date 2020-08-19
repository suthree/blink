# -*- coding: utf-8 -*-

'''

Created on 2017-6-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class CulitemAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.afterSaleServiceDec = None
        self.alertQty = None
        self.assortCode = None
        self.auditFlag = None
        self.brandCode = None
        self.categoryCode = None
        self.cmTitle = None
        self.detailModule = None
        self.freightTemplateId = None
        self.introduction = None
        self.invQty = None
        self.itemCode = None
        self.pars = None
        self.price = None
        self.productName = None
        self.saleCatalogCode = None
        self.saleDate = None
        self.saleSet = None
        self.sellPoint = None
        self.supplierImgAUrl = None
        self.supplierImgBUrl = None
        self.supplierImgCUrl = None
        self.supplierImgDUrl = None
        self.supplierImgEUrl = None
        
        self.setParamRule({
        	'afterSaleServiceDec':{'allow_empty':False},
        	'brandCode':{'allow_empty':False},
        	'categoryCode':{'allow_empty':False},
        	'cmTitle':{'allow_empty':False},
        	'freightTemplateId':{'allow_empty':False},
        	'invQty':{'allow_empty':False},
        	'price':{'allow_empty':False},
        	'productName':{'allow_empty':False},
        	'saleCatalogCode':{'allow_empty':False},
        	'saleSet':{'allow_empty':False},
        	'supplierImgAUrl':{'allow_empty':False},
        	'supplierImgBUrl':{'allow_empty':False},
        	'supplierImgCUrl':{'allow_empty':False},
        	'supplierImgDUrl':{'allow_empty':False},
        	'supplierImgEUrl':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addCulitem'

    def getApiMethod(self):

        return 'suning.custom.culitem.add'



