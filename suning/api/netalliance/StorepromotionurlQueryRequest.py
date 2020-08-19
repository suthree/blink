# -*- coding: utf-8 -*-

'''

Created on 2017-6-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class StorepromotionurlQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.adBookId = None
        self.commCode = None
        self.mertCode = None
        
        self.setParamRule({
        	'adBookId':{'allow_empty':False},
        	'mertCode':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryStorepromotionurl'

    def getApiMethod(self):

        return 'suning.netalliance.storepromotionurl.query'



