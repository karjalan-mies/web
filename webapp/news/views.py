from flask import Blueprint, current_app, render_template
from webapp.news.models import News
from webapp.weather import weather_by_city

blueprint = Blueprint('news', __name__)

@blueprint.route('/')
@blueprint.route('/index')
def index():
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    news_list = News.query.order_by(News.date.desc()).all()
    title = 'Новости Python'
    return render_template('index.html', title=title, weather=weather, news_list=news_list)