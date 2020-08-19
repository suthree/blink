# -*- coding: utf-8 -*-

'''

Created on 2014-8-22

@author: suning

'''

from suning.api.abstract import AbstractApi



class ShopcategoryQueryRequest(AbstractApi):

    '''

    '''

    def __init__(self):

        AbstractApi.__init__(self)

        self.pageSize = None
        self.pageNo = None



    def getApiBizName(self):

        return 'shopCategory'



    def getApiMethod(self):

        return 'suning.custom.shopcategory.query'



