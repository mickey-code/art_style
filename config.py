import os

class Config:
    pass

class PodConfig(Config):
    
    pass
class DevConfig(Config):
    DEBUG = True
    
# config_options = {
#     # 'development':DevConfig,
#     # 'production':ProdConfig
