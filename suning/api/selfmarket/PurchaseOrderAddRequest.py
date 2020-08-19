# -*- coding: utf-8 -*-

'''

Created on 2016-3-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class PurchaseOrderAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.supplierCode = None
        self.orderCode = None
        self.itemNo = None
        self.confirmType = None
        self.confirmDeliveryDate = None
        
        self.setParamRule({
        	'supplierCode':{'allow_empty':False},
        	'orderCode':{'allow_empty':False},
        	'itemNo':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'purchaseOrderConfirm'

    def getApiMethod(self):

        return 'suning.purchaseorder.confirm'



