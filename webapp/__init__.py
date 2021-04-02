from flask import Flask, render_template
from flask import current_app

from webapp.forms import LoginForm
from webapp.models import db, News
from webapp.weather import weather_by_city

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
        news_list = News.query.order_by(News.date.desc()).all()
        title = 'Новости Python'
        return render_template('index.html', title=title, weather=weather, news_list=news_list)

    @app.route('/login')
    def login():
        title = 'Страница авторизации'
        login_form = LoginForm()
        return render_template('login,html', title=title, login_form=login_form)

    return app.run(debug=True)
