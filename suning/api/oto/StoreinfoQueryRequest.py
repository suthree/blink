# -*- coding: utf-8 -*-

'''

Created on 2016-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class StoreinfoQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageNo = None
        self.pageSize = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryStoreinfo'

    def getApiMethod(self):

        return 'suning.oto.storeinfo.query'



