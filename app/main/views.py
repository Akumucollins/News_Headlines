from flask import render_template,request,redirect,url_for
from app.request import get_sources
from . import main
from ..request import get_sources,article_source,get_category

# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and
    its data
    '''
    general_sources = get_sources('general')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    business_sources = get_sources('business')
    health_sources = get_sources('health')
    science_sources = get_sources('science')

    title = 'Highlight News Source '
    return render_template('index.html',title=title,business = business_sources,health=health_sources,science=science_sources,sports = sports_sources, technology = technology_sources,entertainment = entertainment_sources ,general=general_sources)

@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    articles = article_source(id)
    return render_template('article.html',articles= articles,id=id )

@main.route('/categories/<category_name>')
def category(category_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(category_name)
    title = f'{category_name}'
    categories = category_name

    return render_template('categories.html',title = title,category = category, categories= category_name)
