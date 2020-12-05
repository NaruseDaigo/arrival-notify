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
    amazon = {"item": "PlayStation5", "url": 'https://www.amazon.co.jp/%E3%82%BD%E3%83%8B%E3%83%BC%E3%83%BB%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%A9%E3%82%AF%E3%83%86%E3%82%A3%E3%83%96%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%86%E3%82%A4%E3%83%B3%E3%83%A1%E3%83%B3%E3%83%88-PlayStation-5-CFI-1000A01/dp/B08GGGBKRQ/ref=sr_1_5?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=AEBBDAPJO8DS&dchild=1&keywords=playstation+5&qid=1606400721&sprefix=playstatio%2Caps%2C315&sr=8-5'}

    get_html(amazon["url"])
