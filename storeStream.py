import tweepy
import json
import sqlite3
from textblob import TextBlob
from secret import *
# Unique code from Twitter

# Boilerplate code here
auth = tweepy.OAuthHandler(secret.consumer_key,secret.consumer_secret)
auth.set_access_token(secret.access_token,secret.access_token_secret)

#Set up Database
conn = sqlite3.connect('twitter.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS TwitterDB")
cur.execute('''
CREATE TABLE IF NOT EXISTS TwitterDB
    (query TEXT, user TEXT, tweet TEXT, dt TEXT, sub TEXT, pol TEXT)''')


api = tweepy.API(auth)

search="Michigan Football"
public_tweets = api.search(search)


def process_or_store(tweet):
	user = tweet.get('user').get('screen_name')
	txt = tweet.get('text')
	dt = tweet.get('created_at')
	tb= TextBlob(txt)
	sub = str(tb.sentiment.subjectivity)
	pol = str(tb.sentiment.polarity)
	sqlstr = "INSERT INTO TwitterDB (user, tweet, dt, sub, pol, query) VALUES ('"+user+ "', '"+txt+"','" + dt+"', '"+sub+"', '"+pol+"', '"+search+"')"
	print (sqlstr)
	try:
		cur.execute(sqlstr)
	except:
		print ("Error on insertion")
	conn.commit()

for tweet in public_tweets:
	process_or_store(tweet._json)


# for status in tweepy.Cursor(api.home_timeline).items(10):
#     # Process a single status
#     process_or_store(status._json) 



# for tweet in tweepy.Cursor(api.user_timeline).items():
# 	process_or_store(tweet._json)


