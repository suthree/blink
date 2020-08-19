# -*- coding: utf-8 -*-

'''

Created on 2017-4-24

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReturngoodsQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.endTime = None
        self.startTime = None
        self.pageSize = None
        self.pageNo = None
        
        self.setParamRule({
        	'endTime':{'allow_empty':False},
        	'startTime':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryReturngoods'

    def getApiMethod(self):

        return 'suning.custom.returngoods.query'



