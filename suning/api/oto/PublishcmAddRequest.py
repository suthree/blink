# -*- coding: utf-8 -*-

'''

Created on 2016-11-16

@author: suning

'''

from suning.api.abstract import AbstractApi



class PublishcmAddRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.sellPoint = None
        self.introduction = None
        self.saleSet = None
        self.saleDate = None
        self.productCode = None
        self.itemCode = None
        self.price = None
        self.assortCode = None
        self.childItem = None
        self.cmTitle = None
        self.supplierImg1Url = None
        self.supplierImg2Url = None
        self.supplierImg3Url = None
        self.supplierImg4Url = None
        self.supplierImg5Url = None
        self.detailModule = None
        self.targetChannel = None
        self.packingList = None
        
        self.setParamRule({
        	})

    def getApiBizName(self):

        return 'addPublishcm'

    def getApiMethod(self):

        return 'suning.oto.publishcm.add'



