# -*- coding: utf-8 -*-

'''

Created on 2017-5-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class ItemAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.supplierImg3Url = None
        self.categoryCode = None
        self.sellPoint = None
        self.supplierImg2Url = None
        self.supplierImg5Url = None
        self.barpic = None
        self.cmTitle = None
        self.supplierImg1Url = None
        self.price = None
        self.supplierImg4Url = None
        self.brandCode = None
        self.productName = None
        self.introduction = None
        self.itemCode = None
        self.childItem = None
        self.pars = None
        self.detailModule = None
        self.packingList = None
        self.ltpic = None
        
        self.setParamRule({
        	'categoryCode':{'allow_empty':False},
        	'sellPoint':{'allow_empty':False},
        	'supplierImg2Url':{'allow_empty':False},
        	'supplierImg5Url':{'allow_empty':False},
        	'cmTitle':{'allow_empty':False},
        	'supplierImg1Url':{'allow_empty':False},
        	'supplierImg4Url':{'allow_empty':False},
        	'brandCode':{'allow_empty':False},
        	'productName':{'allow_empty':False},
        	'ltpic':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addItem'

    def getApiMethod(self):

        return 'suning.saleoff.item.add'



