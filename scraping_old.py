import requests
from bs4 import BeautifulSoup
import time

HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}

def rakutenbooks_check(url):
    res = requests.get(url ,headers=HEADERS)
    soup = BeautifulSoup(res.content,'html.parser')

    try:
        str = soup.find('button',class_='new_addToCart').get_text()
        if str == stock_word:
            result = 1
        else:
            print("error")
            exit(1)
    except:
        result = 0

    return result

#  URL配列作成
rakuten_books = ["https://books.rakuten.co.jp/rb/16462859/?bkts=1&l-id=search-c-item-text-01", "https://books.rakuten.co.jp/rb/16462860/?bkts=1&l-id=search-c-item-text-02", "https://books.rakuten.co.jp/rb/15984061/"]

print("### Rakutenブックス ###")
stock_word = '買い物かごに入れる'
for url in rakuten_books:
    result = rakutenbooks_check(url)
    if result == 1:
        print("在庫あり")
        print(f"URL: {url}")
    elif result == 0:
        print("入荷待ち")
        print(f"URL: {url}")


"""if __name__ == "__main__":
	while True:
		new_stock ()
		time.sleep(60)"""
