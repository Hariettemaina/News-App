from flask import render_template
from . import main
from ..request import get_news,get_sources

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news = get_news() 
    title = 'JollyNews'
    return render_template('index.html', title = title,articles = news)
@main.route('/sources')
def sources():

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_sources()
    return render_template('news.html',sources = news)