# -*- coding: utf-8 -*-

'''

Created on 2017-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReturnpartorderAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.skus = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addReturnpartorder'

    def getApiMethod(self):

        return 'suning.govbus.returnpartorder.add'



