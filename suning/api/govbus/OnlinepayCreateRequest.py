# -*- coding: utf-8 -*-

'''

Created on 2017-12-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class OnlinepayCreateRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.channelType = None
        self.backUrl = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	'channelType':{'allow_empty':False},
        	'backUrl':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'createOnlinepay'

    def getApiMethod(self):

        return 'suning.govbus.onlinepay.create'



