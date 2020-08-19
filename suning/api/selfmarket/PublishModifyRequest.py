# -*- coding: utf-8 -*-

'''

Created on 2017-1-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class PublishModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        self.itemCode = None
        self.cmTitle = None
        self.sellPoint = None
        self.supplierImgUrl = None
        self.introduction = None
        self.detailModule = None
        self.packingList = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyPublish'

    def getApiMethod(self):

        return 'suning.selfmarket.publish.modify'



