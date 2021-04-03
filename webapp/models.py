from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    text = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f'News {self.title} {self.url}'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, nullable=False)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10))

    def set_password(self, password):
        self.password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password)


    @property
    def is_admin(self):
        return self.role == 'admin'


    def __repr__(self):
        return f'<User {self.username}>'
