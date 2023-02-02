import bs4
import requests

from fake_headers import Headers

from logger_2 import logger

header = Headers(
        browser="chrome",
        os="win",
        headers=True
    )
HEADERS = header.generate()
URL = "https://habr.com/ru/all"
URL1 = "https://habr.com"
KEYWORDS = ["дизайн", "фото", "SQL", "python", "тестирование", "Фриланс", "Транспорт"]

response = requests.get(URL, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all("article")

@logger("func_log.log")
def func():
    for article in articles:

        title = article.find("h2").find("span").text
        hubs = article.find_all(class_="tm-article-snippet__hubs-item-link")
        art_body = article.find(class_="tm-article-body tm-article-snippet__lead").text

        separated_hubs = []
        for hub in hubs:
            hub = hub.text.strip().split(" ")
            separated_hubs += hub
        
        
        for word in KEYWORDS:
            if word in art_body or word in title or word in separated_hubs:
                href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
                art_date = article.find("time").attrs["title"]
                result = f"{art_date} - {title} - {URL1}{href}"
                print(result)
   
if __name__ == '__main__':
    func()
