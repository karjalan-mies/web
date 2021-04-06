from webapp.db import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    text = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f'News {self.title} {self.url}'