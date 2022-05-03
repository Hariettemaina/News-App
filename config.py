import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey=3da8ea86f3e84d3fb09b052a32f9f1fc'
    NEWS_API_KEY = os.environ.get('3da8ea86f3e84d3fb09b052a32f9f1fc')



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}