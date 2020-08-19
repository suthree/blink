# -*- coding: utf-8 -*-

'''

Created on 2017-2-17

@author: suning

'''

from suning.api.abstract import AbstractApi



class DisagreerejectedModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.notReason = None
        self.omsOrderItemNo = None
        self.supplierCode = None
        
        self.setParamRule({
        	'notReason':{'allow_empty':False},
        	'omsOrderItemNo':{'allow_empty':False},
        	'supplierCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'modifyDisagreerejected'

    def getApiMethod(self):

        return 'suning.selfmarket.disagreerejected.modify'



