db_username = "root"
db_password = ""
database = "db_user"


class Config(object):
    """
    Common configurations
    """

    DEBUG = False
    SECRET_KEY = "secret-key"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + db_username + ':' + db_password + '@localhost/' + database
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
