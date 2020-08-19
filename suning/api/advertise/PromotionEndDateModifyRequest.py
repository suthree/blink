# -*- coding: utf-8 -*-

'''

Created on 2016-10-19

@author: suning

'''

from suning.api.abstract import AbstractApi



class PromotionEndDateModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.promotionId = None
        self.promotionEndDate = None
        
        self.setParamRule({
        	'promotionId':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'modifyPromotionEndDate'

    def getApiMethod(self):

        return 'suning.advertise.promotionenddate.modify'



