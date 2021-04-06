from datetime import datetime

import requests
from bs4 import BeautifulSoup

from webapp.db import db
from webapp.news.models import News

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        return False


def get_python_news():
    html = get_html('https://www.python.org/blogs/')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_ = 'list-recent-posts').findAll('li')
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            date = news.find('time')['datetime']
            try:
                date = datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                date = datetime.now()
            save_news(title, url, date)


def save_news(title, url, date):
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        new_news = News(title=title, url=url, date=date)
        db.session.add(new_news)
        db.session.commit()
