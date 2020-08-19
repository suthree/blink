# -*- coding: utf-8 -*-

'''

Created on 2016-11-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class BatchProdSaleStatusGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.skuIds = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getBatchProdSaleStatus'

    def getApiMethod(self):

        return 'suning.govbus.batchprodsalestatus.get'



