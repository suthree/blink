# -*- coding: utf-8 -*-

'''

Created on 2017-8-14

@author: suning

'''

from suning.api.abstract import AbstractApi



class MessageGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.type = None
        
        self.setParamRule({
        	'type':{'allow_empty':False}
        	})

    def getApiBizName(self):

        return 'getMessage'

    def getApiMethod(self):

        return 'suning.govbus.message.get'



