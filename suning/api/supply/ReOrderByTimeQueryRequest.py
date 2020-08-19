# -*- coding: utf-8 -*-

'''

Created on 2016-3-25

@author: suning

'''

from suning.api.abstract import AbstractApi



class ReOrderByTimeQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.startTime = None
        self.endTime = None
        self.orderItemStatus = None
        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'queryReOrderByTime'

    def getApiMethod(self):

        return 'suning.supply.reorderbytime.query'



