from credential import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
from requests_oauthlib import OAuth1Session
from http import HTTPStatus
from datetime import datetime

def post_tweet(body):
    # 認証処理
    twitter = OAuth1Session(
        CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
    )
    # ツイート処理
    res = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params={"status": body})
    print(res)

    # エラー処理
    if res.status_code == HTTPStatus.OK:
        print("Successfuly posted")
    else:
        print(f"Failed: {res.status_code}")

def main():
    # body = "テスト投稿2"
    now = "@tos lol"
    post_tweet(now)


if __name__ == '__main__':
    main()
