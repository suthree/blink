# -*- coding: utf-8 -*-

'''

Created on 2017-5-4

@author: suning

'''

from suning.api.abstract import AbstractApi



class InvoiceConfirmRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.applyForInvoiceReqDTO = None
        self.orderInfoDTO = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'confirmInvoice'

    def getApiMethod(self):

        return 'suning.govbus.invoice.confirm'



