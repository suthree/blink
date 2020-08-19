#!usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2014年6月5日
配置项
@author: dd
'''
class Const():
    VERSION = "v1.2"
    
    SDK_VERSION = "suning-sdk-python-beta0.1"
    
    #超时时间
    TIMEOUT = 10
    
    # api访问路径
    API_URI = "/api/http/sopRequest"
    
    #api请求格式，此sdk目前只支持json
    API_FORMAT = "json"
    
    #api 访问域名或IP
    DOMAIN = "openpre.cnsuning.com"
    
    #api 访问端口
    PORT = 80
    
    # API appkey 
    #APPKEY="4be597ae2ab497a06a75e2f8bea6f089"
    APPKEY = "6c84c582f917e3f36fc372fe9cdad1e7"
    
    # API appsecret 
    # APPSECRET="dd565941167025fbe7431912133fbecd"
    APPSECRET= "f7b9058df322de327900640998d278d5"
    
    #AccessToken 默认为空
    ACCESS_TOKEN = None
    