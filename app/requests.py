import urllib.request,json
from .models import Source, Article

# Getting api key
api_key = None

def configure_request(app):
    global api_key
    api_key = app.config['NEWS_API_KEY']

def get_sources():
    '''
    Function to get json response to the url request for news sources
    '''
    get_sources_url = 'https://newsapi.org/v1/sources'

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results

def process_sources(source_list):
    '''
    Function  that processes the source results and transform them to a list of objects
    
    Args:
        source_list: A list of dictionaries that contain source details
    
    Returns :
        source_results: A list of source objects
    '''
    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')

        source_object = Source(id,name,description)

        source_results.append(source_object)

    return source_results

def get_articles(id):
    '''
    Function to get a source and it's articles
    '''
    get_articles_url = 'https://newsapi.org/v1/articles?source={}&apiKey={}'.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results

# def process_articles(article_list):
#     '''
#     Function that processes the article results and transform them to a list of objects
    
#     Args:
#         article_list: A list of dictionaries that contain article details
    
#     Returns :
#         article_results: A list of article objects
#     '''
#     article_results = []

#     for article_item in article_list:
#         source = article_item.get('source')
#         title = article_item.get('title')
#         urlToImage = article_item.get('urlToImage')
#         description = article_item.get('description')
#         urlToArticle = article_item.get('url')
#         publishedAt = article_item.get('publishedAt')

#         if publishedAt != None:

#             # Call publish_date_format method to convert date to a display-friendly format
#             date_to_display = Article.publish_date_format(publishedAt)


#             article_object = Article(source,title,urlToImage,description,urlToArticle,date_to_display)

#             article_results.append(article_object)

#     return article_results
