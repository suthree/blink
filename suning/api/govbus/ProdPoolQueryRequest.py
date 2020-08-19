# -*- coding: utf-8 -*-

'''

Created on 2016-8-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class ProdPoolQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.categoryId = None
        
        self.setParamRule({
        	'categoryId':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryProdPool'

    def getApiMethod(self):

        return 'suning.govbus.prodpool.query'



