# -*- coding: utf-8 -*-

'''

Created on 2017-5-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class OrdersplitAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderSplit = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addOrdersplit'

    def getApiMethod(self):

        return 'suning.selfmarket.ordersplit.add'



