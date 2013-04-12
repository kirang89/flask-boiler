# Add your configuration here


class Config(object):
    NAME = 'FOO'
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    NAME = 'Kiran'


class DevelopmentConfig(Config):
    NAME = 'Developer1234'
    DEBUG = True


class TestingConfig(Config):
    NAME = 'Tester123'
    TESTING = True
