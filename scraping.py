from credential import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
import requests
from bs4 import BeautifulSoup
import time
import sys
import datetime
import tweepy

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#  PCから接続
HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}

def tweet(item, url):
    #  Tweetする時刻の設定
    now_time = datetime.datetime.now().strftime('%H:%M:%S')

    tweet = ""
    tweet += f"「{item}」が入荷されました\n"
    tweet += f"URL: {url}\n"
    tweet += f"時刻: {now_time}\n#PS5 #PlayStation5 #PS5抽選 #PS5予約"
    print(tweet)
    # api.update_status(tweet)

def rakutenbooks_check(url):
    res = requests.get(url ,headers=HEADERS)
    soup = BeautifulSoup(res.content,'html.parser')
    stock_word = '買い物かごに入れる'

    try:
        str = soup.find('button',class_='new_addToCart').get_text()
        if str == stock_word:
            result = 1
        else:
            print("error")
            sys.exit(1)
    except:
        result = 0

    return result

def rakuten_run():
    rakuten_books = [{"item": "PlayStation5", "url": 'https://a.r10.to/hwl9PM'}, \
                     {"item": "PlayStation5 デジタル・エディション", "url": 'https://a.r10.to/hVZxyj'}, \
                     {"item": "ポケットモンスター ソード", "url": 'https://a.r10.to/hV9Bt2'}]

    print("\n### Rakutenブックス ###")
    for page in rakuten_books:
        if rakutenbooks_check(page["url"]) == 1:
            print("入荷検知")
            tweet(page["item"], page["url"])

def amazon_check(url):
    res = requests.get(url ,headers=HEADERS)
    soup = BeautifulSoup(res.content,'html.parser')
    stock_word = 'カートに入れる'

    try:
        str = soup.find_all('span',class_='a-button-text')
        strlist = [x.text for x in str]
        if strlist[1] == stock_word:
            result = 1
        else:
            result = 0
    except:
        result = 0

    return result

def amazon_run():
    amazon = [{"item": "PlayStation5", "url": 'https://www.amazon.co.jp/%E3%82%BD%E3%83%8B%E3%83%BC%E3%83%BB%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%A9%E3%82%AF%E3%83%86%E3%82%A3%E3%83%96%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%86%E3%82%A4%E3%83%B3%E3%83%A1%E3%83%B3%E3%83%88-PlayStation-5-CFI-1000A01/dp/B08GGGBKRQ/ref=sr_1_5?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=AEBBDAPJO8DS&dchild=1&keywords=playstation+5&qid=1606400721&sprefix=playstatio%2Caps%2C315&sr=8-5'}, \
              {"item": "PlayStation5 デジタル・エディション", "url": 'https://www.amazon.co.jp/%E3%82%BD%E3%83%8B%E3%83%BC%E3%83%BB%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%A9%E3%82%AF%E3%83%86%E3%82%A3%E3%83%96%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%86%E3%82%A4%E3%83%B3%E3%83%A1%E3%83%B3%E3%83%88-PlayStation-5-%E3%83%87%E3%82%B8%E3%82%BF%E3%83%AB%E3%83%BB%E3%82%A8%E3%83%87%E3%82%A3%E3%82%B7%E3%83%A7%E3%83%B3-CFI-1000B01/dp/B08GGF7M7B/ref=sr_1_7?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=AEBBDAPJO8DS&dchild=1&keywords=playstation+5&qid=1606400721&sprefix=playstatio%2Caps%2C315&sr=8-7'}, \
              {"item": "PlayStation5【Amazon.co.jp特典】オリジナルデザインエコバッグ", "url": 'https://www.amazon.co.jp/%E3%82%BD%E3%83%8B%E3%83%BC%E3%83%BB%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%A9%E3%82%AF%E3%83%86%E3%82%A3%E3%83%96%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%86%E3%82%A4%E3%83%B3%E3%83%A1%E3%83%B3%E3%83%88-PlayStation-5-CFI-1000A01-%E3%80%90Amazon-co-jp%E7%89%B9%E5%85%B8%E3%80%91%E3%82%AA%E3%83%AA%E3%82%B8%E3%83%8A%E3%83%AB%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3%E3%82%A8%E3%82%B3%E3%83%90%E3%83%83%E3%82%B0/dp/B08GGGCH3Y/ref=sr_1_6?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=AEBBDAPJO8DS&dchild=1&keywords=playstation+5&qid=1606400721&sprefix=playstatio%2Caps%2C315&sr=8-6'},\
              {"item": "PlayStation5　デジタル・エディション【Amazon.co.jp特典】オリジナルデザインエコバッグ", "url": 'https://www.amazon.co.jp/PlayStation-5-%E3%83%87%E3%82%B8%E3%82%BF%E3%83%AB%E3%83%BB%E3%82%A8%E3%83%87%E3%82%A3%E3%82%B7%E3%83%A7%E3%83%B3-CFI-1000B01-%E3%80%90Amazon-co-jp%E7%89%B9%E5%85%B8%E3%80%91%E3%82%AA%E3%83%AA%E3%82%B8%E3%83%8A%E3%83%AB%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3%E3%82%A8%E3%82%B3%E3%83%90%E3%83%83%E3%82%B0/dp/B08GGCGS39/ref=sr_1_2?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=PlayStation+5+%E3%83%87%E3%82%B8%E3%82%BF%E3%83%AB%E3%83%BB%E3%82%A8%E3%83%87%E3%82%A3%E3%82%B7%E3%83%A7%E3%83%B3+%28CFI-1000B01%29&qid=1606377898&s=videogames&sr=1-2'},\
              {"item": "ポケットモンスター ソード", "url": 'https://www.amazon.co.jp/%E4%BB%BB%E5%A4%A9%E5%A0%82-%E3%83%9D%E3%82%B1%E3%83%83%E3%83%88%E3%83%A2%E3%83%B3%E3%82%B9%E3%82%BF%E3%83%BC-%E3%82%BD%E3%83%BC%E3%83%89-Switch/dp/B07V3KK93X/ref=sr_1_1?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%82%BD%E3%83%BC%E3%83%89&qid=1606401778&sr=8-1'}]

    print("\n### Amazon.co.jp ###")
    for page in amazon:
        if amazon_check(page["url"]) == 1:
            print("入荷検知")
            tweet(page["item"], page["url"])

if __name__ == "__main__":
    time_counter = 0
    while time_counter <= 540:
        rakuten_run()
        amazon_run()
        time_counter += 60
        time.sleep(60)
