# -*- coding: utf-8 -*-

'''

Created on 2017-1-12

@author: suning

'''

from suning.api.abstract import AbstractApi



class MainproductModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.productCode = None
        self.correctData = None
        
        self.setParamRule({
        	'productCode':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyMainproduct'

    def getApiMethod(self):

        return 'suning.selfmarket.mainproduct.modify'



