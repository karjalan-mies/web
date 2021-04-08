from datetime import datetime

from bs4 import BeautifulSoup


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

