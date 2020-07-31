import tweepy
import time
from datetime import datetime


consumerKey = *****'
consumerSecret = *****'
accessKey = *****
accessSecret = *****

auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.set_access_token(accessKey,accessSecret)

api = tweepy.API(auth)


FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME,'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def write_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME))
    for tweet in reversed(tweets):
        global i
        print(str(tweet.id) + ' - ' + tweet.text)
        api.update_status('@' + tweet.user.screen_name + " Auto reply, like, and retweet work :)" + str(i), tweet.id)
        if not tweet.favorited:
            api.create_favorite(tweet.id)
        if not tweet.retweeted:
            api.retweet(tweet.id)
        write_last_seen(FILE_NAME, tweet.id)

def tweet_now(api, text):
    api.update_status(text)
    
i = 0
while True:
    
    print('+++++++++++Start++++++++++' + str(i))
    text = "Current Date and Time is : " + str(datetime.today())
    
    if (i % (1 * 60 * 2) == 0 ):
        tweet_now(api, text) 
    i = i + 1

    if (i % 5) :
        reply()

    if ( i == 60 * 60 *24):
        i = 0
    time.sleep(1)
