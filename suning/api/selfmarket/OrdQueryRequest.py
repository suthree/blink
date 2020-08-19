# -*- coding: utf-8 -*-

'''

Created on 2017-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrdQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endTime = None
        self.orderItemStatus = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        self.supplierCode = None
        
        self.setParamRule({
        	'endTime':{'allow_empty':False},
        	'orderItemStatus':{'allow_empty':False},
        	'startTime':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryOrd'

    def getApiMethod(self):

        return 'suning.selfmarket.ord.query'



