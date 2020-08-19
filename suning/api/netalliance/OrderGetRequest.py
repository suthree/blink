# -*- coding: utf-8 -*-

'''

Created on 2018-2-7

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrderGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderCode = None
        
        self.setParamRule({
        	'orderCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getOrder'

    def getApiMethod(self):

        return 'suning.netalliance.order.get'



