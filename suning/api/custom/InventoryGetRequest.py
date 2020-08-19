# -*- coding: utf-8 -*-

'''

Created on 2017-4-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class InventoryGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.invCode = None
        self.productCode = None
        
        self.setParamRule({
        	'invCode':{'allow_empty':False},
        	'productCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getInventory'

    def getApiMethod(self):

        return 'suning.custom.inventory.get'



