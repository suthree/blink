# -*- coding: utf-8 -*-

'''

Created on 2017-6-6

@author: suning

'''

from suning.api.abstract import AbstractApi



class CulitemdetailQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.itemCode = None
        self.productCode = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryCulitemdetail'

    def getApiMethod(self):

        return 'suning.custom.culitemdetail.query'



