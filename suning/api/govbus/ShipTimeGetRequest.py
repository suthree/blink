# -*- coding: utf-8 -*-

'''

Created on 2017-5-9

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShipTimeGetRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.cityId = None
        self.districtId = None
        self.townId = None
        self.addrDetail = None
        self.skuIds = None
        
        self.setParamRule({
        	'cityId':{'allow_empty':False},
        	'districtId':{'allow_empty':False},
        	'addrDetail':{'allow_empty':False},
        	})

    def getApiBizName(self):

        return 'getShipTime'

    def getApiMethod(self):

        return 'suning.govbus.shiptime.get'



