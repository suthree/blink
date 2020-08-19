# -*- coding: utf-8 -*-

'''

Created on 2018-2-7

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endTime = None
        self.orderLineStatus = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryOrder'

    def getApiMethod(self):

        return 'suning.netalliance.order.query'



