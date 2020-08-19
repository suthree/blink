# -*- coding: utf-8 -*-

'''

Created on 2017-6-23

@author: suning

'''

from suning.api.abstract import AbstractApi



class HomepagepositionurlQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'queryHomepagepositionurl'

    def getApiMethod(self):

        return 'suning.netalliance.homepagepositionurl.query'



