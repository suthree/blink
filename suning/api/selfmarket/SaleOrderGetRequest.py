# -*- coding: utf-8 -*-

'''

Created on 2017-7-31

@author: suning

'''

from suning.api.abstract import AbstractApi



class SaleOrderGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderItemId = None
        self.supplierCode = None
        
        self.setParamRule({
        	'orderItemId':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getSaleOrder'

    def getApiMethod(self):

        return 'suning.selfmarket.saleorder.get'



