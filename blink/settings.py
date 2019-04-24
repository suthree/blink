# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
# from environs import Env

# env = Env()
# env.read_env()

# ENV = env.str('FLASK_ENV', default='production')
# DEBUG = ENV == 'development'
# SECRET_KEY = env.str('SECRET_KEY')
# BCRYPT_LOG_ROUNDS = env.int('BCRYPT_LOG_ROUNDS', default=13)
# DEBUG_TB_ENABLED = DEBUG
# DEBUG_TB_INTERCEPT_REDIRECTS = False
# CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# WEBPACK_MANIFEST_PATH = 'webpack/manifest.json'


class DefaultConfig(object):
    DEBUG = True
    ENV = 'development'
    SECRET_KEY = 'lifeistooshorttowait'

    SESSION_COOKIE_PATH='/'
    SESSION_COOKIE_HTTPONLY = True
    #SESSION_COOKIE_SECURE = True
    #SESSION_COOKIE_NAME = 'themissing'
    # PERMANENT_SESSION_LIFETIME = datetime.timedelta(180)
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@localhost/dev'

    BCRYPT_LOG_ROUNDS = 13
    DEBUG_TB_ENABLED = DEBUG
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # DATABASE_URL = 'sqlite:////tmp/dev.db'

class TestConfig(DefaultConfig):
    DEBUG = False
    ENV = 'test'
    CSRF_ENABLED = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@localhost/test'



class ProductionConfig(DefaultConfig):
    
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@localhost/prd'