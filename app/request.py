import urllib.request,json
from .model import News,Sources


# Getting api key
api_key = None
# Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        

        news_results = None
        
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            # print(news_results_list)
            news_results = process_results(news_results_list)
           


    return news_results
def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        content = news_item.get('content')
        publishedAt = news_item.get('publishedAt')

        
        news_object = News(title,description,urlToImage,content,publishedAt)
        #print(news_object)
        news_results.append(news_object)
        # print(news_results)

    return news_results
#sources
def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    # get_news_url = base_url.format(api_key)
    get_sources_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=3da8ea86f3e84d3fb09b052a32f9f1fc'

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        

        sources_results = None
        
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            # print(news_results_list)
            sources_results = process_results(sources_results_list)
           


    return sources_results
def process_results(sources_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    sources_results = []
    for sources_item in sources_list:
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
       

        
        sources_object = Sources(name,description,url)
        #print(sources_object)
        sources_results.append(sources_object)
        # print(news_results)

    return sources_results