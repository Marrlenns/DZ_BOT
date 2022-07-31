import requests
from bs4 import BeautifulSoup

URL = "https://kaktus.media/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('a', class_='Dashboard-Content-Card--name')
    news = []
    for item in items:
        news.append({
            'title': item.find("span", class_='Dashboard-Content-Card--countComments tolstoy-comments-count').getText(),
            'Companytitle': item.find("a", class_='CompanyArticles--title').getText(),
            'upper': item.find("div", class_='Up Up----view').getText(),

        })
    return news


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = []
        for page in range(1, 3):
            html = get_html(f"{URL}page1_{page}.php")
            answer.extend(get_data(html.text))
        return answer
    else:
        raise Exception("Error in parser!")