# -*- coding: utf-8 -*-

'''

Created on 2017-7-20

@author: suning

'''

from suning.api.abstract import AbstractApi



class CustompromotionurlQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.adBookId = None
        self.visitUrl = None
        
        self.setParamRule({
        	'adBookId':{'allow_empty':False},
        	'visitUrl':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'queryCustompromotionurl'

    def getApiMethod(self):

        return 'suning.netalliance.custompromotionurl.query'



