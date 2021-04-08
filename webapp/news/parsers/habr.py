from datetime import datetime

from bs4 import BeautifulSoup

from webapp.news.parsers.utils import get_html, save_news

def get_habr_snippets():
    html = get_html('https://habr.com/ru/search/?target_type=posts&q=%5Bpython%5D&order_by=date')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_ = 'content-list_posts').findAll('li', class_='content-list__item_post')
        for news in all_news:
            title = news.find('a', class_='post__title_link').text
            url = news.find('a', class_='post__title_link')['href']
            date = news.find('span', class_='post__time').text
            print(title, url, date)
            '''
            try:
                date = datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                date = datetime.now()
            save_news(title, url, date)
            '''