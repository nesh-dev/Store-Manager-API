import os



class Config(object):

    # Base Config

    DEBUG = False
    # get secret key from enviroment variables
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_BLACKLIST_ENABLED = True
    POSTGRES_DATABASE_URI = os.getenv('DATABASE_URL')

    Testing = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    Testing = True
    DEBUG = True
    POSTGRES_DATABASE_URI = os.getenv('TEST_DATABASE_URL')


class ProductionConfig(Config):
    Testing = False
    DEBUG = False
    

# assign configurations to a dictionary
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestConfig
}
