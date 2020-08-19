# -*- coding: utf-8 -*-

'''

Created on 2017-1-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class ApplyAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.categoryCode = None
        self.brandCode = None
        self.productName = None
        self.sellPoint = None
        self.itemCode = None
        self.introduction = None
        self.pars = None
        self.childItem = None
        self.detailModule = None
        self.cmTitle = None
        self.supplierImgUrl = None
        self.packingList = None
        self.barpic = None
        
        self.setParamRule({
        	'categoryCode':{'allow_empty':False},
        	'brandCode':{'allow_empty':False},
        	'productName':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addApply'

    def getApiMethod(self):

        return 'suning.selfmarket.apply.add'



