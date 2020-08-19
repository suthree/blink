# -*- coding: utf-8 -*-

'''

Created on 2017-5-11

@author: suning

'''

from suning.api.abstract import AbstractApi



class MylibarybatchQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.categoryCode = None
        self.brandCode = None
        self.status = None
        self.startTime = None
        self.endTime = None
        self.pageNo = None
        self.pageNo = None
        self.pageNo = None
        self.pageNo = None
        self.pageSize = None
        self.pageSize = None
        self.pageSize = None
        self.pageSize = None
        
        self.setParamRule({
        	'categoryCode':{'allow_empty':False},
        	'brandCode':{'allow_empty':False},
        	'status':{'allow_empty':False},
        	'startTime':{'allow_empty':False},
        	'endTime':{'allow_empty':False},
        	'pageNo':{'allow_empty':False},
        	'pageNo':{'allow_empty':False},
        	'pageNo':{'allow_empty':False},
        	'pageNo':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'pageSize':{'allow_empty':False},
        	'pageSize':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryMylibarybatch'

    def getApiMethod(self):

        return 'suning.saleoff.mylibarybatch.query'



