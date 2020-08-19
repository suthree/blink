# -*- coding: utf-8 -*-

'''

Created on 2017-6-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class CulitemcontentreviseModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.afterSaleServiceDec = None
        self.assortCode = None
        self.cmTitle = None
        self.detailModule = None
        self.freightTemplateId = None
        self.introduction = None
        self.itemCode = None
        self.productCode = None
        self.salesDate = None
        self.saleSet = None
        self.sellPoint = None
        self.supplierImgAUrl = None
        self.supplierImgBUrl = None
        self.supplierImgCUrl = None
        self.supplierImgDUrl = None
        self.supplierImgEUrl = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyCulitemcontentrevise'

    def getApiMethod(self):

        return 'suning.custom.culitemcontentrevise.modify'



