# -*- coding: utf-8 -*-

'''

Created on 2017-5-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class LeaguerstatusAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.orderId = None
        self.orderItemId = None
        self.iqStatus = None
        
        self.setParamRule({
        	'orderId':{'allow_empty':False},
        	'orderItemId':{'allow_empty':False},
        	'iqStatus':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'addLeaguerstatus'

    def getApiMethod(self):

        return 'suning.selfmarket.leaguerstatus.add'



