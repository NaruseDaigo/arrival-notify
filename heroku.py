from credential import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
import datetime
import time
import tweepy

def main():
    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)


    tw = "現在の時刻をお知らせします。\n"
    tw += datetime.datetime.now().strftime('%H:%M:%S')
    api.update_status(tw)

if __name__ == "__main__":
    main()
