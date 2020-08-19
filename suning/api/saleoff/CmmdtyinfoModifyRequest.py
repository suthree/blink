# -*- coding: utf-8 -*-

'''

Created on 2018-1-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class CmmdtyinfoModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.afterSaleServiceDec = None
        self.childItem = None
        self.cmTitle = None
        self.detailModule = None
        self.introduction = None
        self.itemCode = None
        self.ltpic = None
        self.packingList = None
        self.productCode = None
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

        return 'modifyCmmdtyinfo'

    def getApiMethod(self):

        return 'suning.saleoff.cmmdtyinfo.modify'



