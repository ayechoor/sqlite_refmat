import tweepy
import json
import sqlite3
from secret import *
# Unique code from Twitter

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#Set up Database
conn = sqlite3.connect('twitter.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS TwitterDB
    (user TEXT, tweet TEXT, dt TEXT)''')


api = tweepy.API(auth)
def process_or_store(tweet):
	user = tweet.get('user').get('screen_name')
	txt = tweet.get('text')
	dt = tweet.get('created_at')
	sqlstr = "INSERT INTO TwitterDB (user, tweet, dt) VALUES ('"+user+ "', '"+txt+"','" + dt+"')"
	print (sqlstr)
	try:
		cur.execute(sqlstr)
	except:
		print ("Error on insertion")
	conn.commit()


for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json) 



for tweet in tweepy.Cursor(api.user_timeline).items():
	process_or_store(tweet._json)


