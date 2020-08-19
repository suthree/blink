# -*- coding: utf-8 -*-

'''

Created on 2017-7-11

@author: suning

'''

from suning.api.abstract import AbstractApi



class SaleOrderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.state = None
        self.supplierCode = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'querySaleOrder'

    def getApiMethod(self):

        return 'suning.selfmarket.saleorder.query'



