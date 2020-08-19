# -*- coding: utf-8 -*-

'''

Created on 2017-7-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class ElectronicInvoiceAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.invoiceCode = None
        self.invoiceData = None
        self.invoiceNo = None
        self.invoiceTime = None
        self.invoiceType = None
        self.orderId = None
        self.productCode = None
        
        self.setParamRule({
        	'invoiceCode':{'allow_empty':False},
        	'invoiceData':{'allow_empty':False},
        	'invoiceNo':{'allow_empty':False},
        	'invoiceTime':{'allow_empty':False},
        	'invoiceType':{'allow_empty':False},
        	'orderId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'addElectronicInvoice'

    def getApiMethod(self):

        return 'suning.custom.electronicinvoice.add'



