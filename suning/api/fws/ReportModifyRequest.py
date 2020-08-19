# -*- coding: utf-8 -*-

'''

Created on 2015-6-8

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReportModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.qtOrderCode = None
        self.qtCode = None
        self.orderDetailId = None
        self.itemCode = None
        self.itemName = None
        self.itemDesc = None
        self.qtType = None
        self.qtStandard = None
        self.qtFile = None
        self.fileName = None
        self.qtExpiry = None
        self.qtOrderStatus = None
        self.isPass = None
        self.described = None
        self.memo = None
        
        self.setParamRule({
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	'logisticExpressId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyReport'

    def getApiMethod(self):

        return 'suning.fws.report.modify'



