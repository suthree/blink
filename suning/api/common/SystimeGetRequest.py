# -*- coding: utf-8 -*-

'''

Created on 2016-11-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class SystimeGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'getSystime'

    def getApiMethod(self):

        return 'suning.common.systime.get'



