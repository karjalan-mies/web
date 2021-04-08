import requests

from webapp.db import db
from webapp.news.models import News

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome / 89.0.4389.86 YaBrowser / 21.3.0.673 Yowser / 2.5 Safari / 537.36'
    }
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        return False

def save_news(title, url, date):
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        new_news = News(title=title, url=url, date=date)
        db.session.add(new_news)
        db.session.commit()
