# -*- coding: utf-8 -*-'''Created on 2014-5-27, Auto Generated @author: momo'''from suning.api.abstract import AbstractApiclass CityQueryRequest(AbstractApi):    '''    '''    def __init__(self):        AbstractApi.__init__(self)        self.nationCode = None    def getApiBizName(self):        return 'city'    def getApiMethod(self):        return 'suning.custom.city.query'