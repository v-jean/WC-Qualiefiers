import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or "too hard to decypher string"

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI") or "mysql+pymysql://root:jplv123.YJ@localhost/qualifiers2022"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URI") or "mysql+pymysql://root:jplv123.YJ@localhost/qualifiers2022"

class TestConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI") or "mysql+pymysql://root:jplv123.YJ@localhost/qualifiers2022"

config_dict = {
    "DEV": DevelopmentConfig,
    "PROD": ProductionConfig,
    "TEST": TestConfig,
    "default": DevelopmentConfig
}