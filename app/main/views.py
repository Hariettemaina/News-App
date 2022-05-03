from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = "FlashNews - HomePage"
    sources = get_sources()
    return render_template('index.html', title=title, sources=sources)

@main.route('/source/<source_id>')
def source(source_id):
    '''
    View source page function that returns a source page and its data
    '''
    title = f"{source_id} page"
    articles = get_articles(source_id)
    return render_template('source.html', title=title, articles=articles)