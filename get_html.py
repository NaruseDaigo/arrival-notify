import requests
from bs4 import BeautifulSoup

#  PCから接続
HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36", \
           "Accept-Language": "ja"
        }

def get_html(url):
    res = requests.get(url ,headers=HEADERS)
    soup = BeautifulSoup(res.content,'html.parser')
    print(str(soup))

if __name__ == "__main__":
    rakuten_books = {"item": "PlayStation5", "url": 'https://a.r10.to/hwl9PM'}

    get_html(rakuten_books["url"])
