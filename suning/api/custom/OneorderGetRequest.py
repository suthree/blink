# -*- coding: utf-8 -*-

'''

Created on 2017-11-15

@author: suning

'''

from suning.api.abstract import AbstractApi



class OneorderGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.sdcsOrderId = None
        
        self.setParamRule({
        	'sdcsOrderId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getOneorder'

    def getApiMethod(self):

        return 'suning.custom.oneorder.get'



