from flask import Flask, render_template, flash, redirect, url_for
from flask import current_app
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_migrate import Migrate

from webapp.forms import LoginForm
from webapp.models import db, News, User
from webapp.weather import weather_by_city


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    migrate = Migrate(app, db)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
        news_list = News.query.order_by(News.date.desc()).all()
        title = 'Новости Python'
        return render_template('index.html', title=title, weather=weather, news_list=news_list)

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = 'Страница авторизации'
        login_form = LoginForm()
        return render_template('login.html', title=title, login_form=login_form)


    @app.route('/process_login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы успешно вошли на сайт')
                return redirect(url_for('index'))

        flash('Не правильное имя пользователя или пароль')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешнь разлогинились')
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет админ!'
        else:
            return 'Ты не админ!'

    return app