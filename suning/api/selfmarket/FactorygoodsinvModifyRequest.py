# -*- coding: utf-8 -*-

'''

Created on 2017-12-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class FactorygoodsinvModifyRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.goodsList = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'modifyFactorygoodsinv'

    def getApiMethod(self):

        return 'suning.selfmarket.factorygoodsinv.modify'



