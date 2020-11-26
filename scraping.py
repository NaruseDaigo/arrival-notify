import requests
from bs4 import BeautifulSoup
import time
import sys
import datetime
import tweepy

#twitterのアクセスキー
consumer_key ="131CgNs8FehB5ydPH9Zxh4e5l"
consumer_secret ="F8BYtKntFMlr27LqcVafmWiUNHzFHtUJjbNXyZTaiTaU9ZewLz"
access_token="1186167005092532224-9nWHbabCA5D1fcVLBPl1Ncgt2tmDwb"
access_token_secret ="odSVQZtPVcgSx2tVUbiB2T7jvcEUmEtGmqKNOKPJg61rJ"

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
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
        print(tweet)
        #  tweetを投稿
        #api.update_status(tweet)

if __name__ == "__main__":
    rakuten_run()
