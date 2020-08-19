# -*- coding: utf-8 -*-

'''

Created on 2017-3-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class PriceQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cityId = None
        self.skus = None
        
        self.setParamRule({
        	'cityId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryPrice'

    def getApiMethod(self):

        return 'suning.govbus.price.query'



