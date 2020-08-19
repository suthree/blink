# -*- coding: utf-8 -*-

'''

Created on 2015-12-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class SaleFormGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.brandCode = None
        self.imei = None
        
        self.setParamRule({
        	'brandCode':{'allow_empty':False},
        	'imei':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getSaleForm'

    def getApiMethod(self):

        return 'suning.selfmarket.saleform.get'



