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
    #  URL配列作成
    #  PS5,PS5デジタルエディション,ポケモンソード
    rakuten_books = [{"url": 'https://a.r10.to/hwl9PM', "item": "PlayStation5"}, \
                     {"url": 'https://a.r10.to/hVZxyj', "item": "PlayStation5 デジタル・エディション"}, \
                     {"url": 'https://a.r10.to/hV9Bt2', "item": "ポケットモンスター ソード"}]

    print("### Rakutenブックス ###")
    for page in rakuten_books:
        result = rakutenbooks_check(page["url"])
        #  Tweetする時刻の設定
        now_time = datetime.datetime.now().strftime('%H:%M:%S')

        tweet = ""
        if result == 1:
            #  tweet内容
            tweet += f"「{page['item']}」が入荷されました\n"
        elif result == 0:
            #  tweet内容
            tweet += f"「{page['item']}」の在庫はありません\n"

        tweet += f"URL: {page['url']}\n"
        tweet += f"時刻: {now_time}\n #PS5 #PlayStation5 #PS5抽選 #PS5予約"
        # print(tweet)
        #  tweetを投稿
        if result == 1:
            api.update_status(tweet)

if __name__ == "__main__":
    rakuten_run()
